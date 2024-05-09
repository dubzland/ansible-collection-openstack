#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: openstack_datastore_version
short_description: Creates a new datastore version for a given datastore type.
description:
  - Creates the datastore version
  - Applies the specified validation rules file
author:
  - Josh Williams (@t3hpr1m3)
requirements:
  - python >= 3.8
  - python-openstackclient
  - python-troveclient
options:
  cloud:
    type: str
    required: true
    description: Name of the cloud in C(clouds.yaml) on the controller.
  manager:
    type: str
    required: true
    description: Trove datastore manager responsible for this version.
    choices:
      - mysql
      - postgresql
      - mariadb
  datastore:
    type: str
    required: true
    description: >-
      Name of the datastore this version belongs to. If the datastore does not
      exist, it will be created.
  version:
    type: str
    required: true
    description: >-
      Datastore version number.  This is the Docker image version that will be
      downloaded and executed in the instance.
  image_tags:
    type: list
    elements: str
    description: >-
      List of tags used to find the appropriate image in Glance.  Mutually
      exclusive with O(image_id).
  image_id:
    type: str
    description: >-
      Glance image ID used for instances. Mutually exclusive with O(image_tags).
  validation_rules:
    type: path
    required: true
    description: >-
      Path on the controller to the configuration validation rules for this
      datastore version.
  state:
    type: str
    default: present
    choices: ["present", "absent", "enabled", "disabled"]
    description: >-
      State of this datastore version.  V(enabled)/V(disabled) control the
      C(--active) flag.
"""

EXAMPLES = """
- name: Create a new MySQL version
  dubzland.openstack.openstack_datastore_version:
    cloud: local
    manager: mysql
    datastore: mysql
    version: "5.7.29"
    image_tags:
      - trove
      - mysql
    validation_rules: /usr/lib/python3/dist-packages/trove/templates/mysql/validation-rules.json
    state: enabled
"""

import json

from ansible.module_utils.basic import AnsibleModule


def _ds_cmd(module, cloud, *args):
    openstack_bin = module.get_bin_path("openstack", required=True)
    cmd = [
        "{openstack_bin}".format(openstack_bin=openstack_bin),
        "--os-cloud={cloud}".format(cloud=cloud),
        "datastore",
    ]
    cmd.extend(args)
    return cmd


class OpenStackDatastoreVersion(object):
    def __init__(self, module, cloud):
        self._module = module
        self._cloud = cloud

    def exists(self, datastore, version):
        cmd = _ds_cmd(
            self._module, self._cloud, "version", "list", datastore, "--format", "json"
        )
        rc, out, err = self._module.run_command(cmd)

        if rc != 0:
            self._module.fail_json(
                msg="Error retrieving list of versions", out=out, err=err, cmd=cmd
            )

        versions = json.loads(out)

        version_data = next((v for v in versions if v["Version"] == version), None)

        if version_data:
            return version_data["ID"]
        else:
            return None

    def find(self, datastore, version):
        cmd = _ds_cmd(
            self._module,
            self._cloud,
            "version",
            "show",
            "--datastore",
            datastore,
            "--format",
            "json",
            version,
        )
        rc, out, err = self._module.run_command(cmd)

        if rc not in [0, 1]:
            self._module.fail_json(
                msg="Error retrieving list of versions", out=out, err=err, cmd=cmd
            )

        if rc == 1:
            return None

        return json.loads(out)

    def show(self, id):
        cmd = _ds_cmd(
            self._module,
            self._cloud,
            "version",
            "show",
            "--format",
            "json",
            id,
        )
        rc, out, err = self._module.run_command(cmd)

        if rc != 0:
            self._module.fail_json(
                msg="Error retrieving version by id", out=out, err=err
            )

        return json.loads(out)

    def delete(self, id):
        cmd = _ds_cmd(self._module, self._cloud, "version", "delete", id)
        rc, out, err = self._module.run_command(cmd)

        if rc != 0:
            self._module.fail_json(
                msg="Error deleting datastore version", out=out, err=err
            )

    def update(self, version_record, state, image_tags, image_id):
        needs_update = False
        args = []

        if state == "disabled" and version_record["active"]:
            args.append("--disable")
            needs_update = True
        elif state == "enabled" and not version_record["active"]:
            args.append("--enable")
            needs_update = True

        if image_tags:
            if version_record["image_tags"].sort() != image_tags.sort():
                args.extend(["--image-tags", ",".join(image_tags)])
                needs_update = True
        if image_id:
            if version_record["image_id"] != image_id:
                args.extend(["--image", image_id])
                needs_update = True

        if needs_update:
            cmd = _ds_cmd(self._module, self._cloud, "version", "set")
            cmd.extend(args)
            cmd.append(version_record["id"])
            rc, out, err = self._module.run_command(cmd)

            if rc != 0:
                self._module.fail_json(
                    msg="Error updating datastore version", out=out, err=err
                )

        return needs_update

    def create(self, manager, datastore, version, state, image_tags, image_id):
        cmd = _ds_cmd(self._module, self._cloud, "version", "create")
        if state != "disabled":
            cmd.extend(["--active"])
        if image_tags:
            cmd.extend(["--image-tags", ",".join(image_tags)])
        cmd.extend([version, datastore, manager])
        if image_id:
            cmd.append(image_id)
        else:
            cmd.append("")

        rc, out, err = self._module.run_command(cmd)

        if rc != 0:
            self._module.fail_json(
                msg="Error creating datastore version", out=out, err=err
            )

        return self.find(datastore, version)


def main():
    argument_spec = dict(
        cloud=dict(type="str", required=True),
        manager=dict(
            type="str", required=True, choices=("mysql", "postgresql", "mariadb")
        ),
        datastore=dict(type="str", required=True),
        version=dict(type="str", required=True),
        image_tags=dict(type="list", elements="str", required=False),
        image_id=dict(type="str", required=False),
        validation_rules=dict(type="path", required=True),
        state=dict(
            default="present", choices=["present", "absent", "enabled", "disabled"]
        ),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=[("image_tags", "image_id")],
        required_one_of=[("image_tags", "image_id")],
    )

    cloud = module.params["cloud"]
    manager = module.params["manager"]
    datastore = module.params["datastore"]
    version = module.params["version"]
    image_tags = module.params["image_tags"]
    image_id = module.params["image_id"]
    validation_rules = module.params["validation_rules"]
    state = module.params["state"]

    datastore_version = OpenStackDatastoreVersion(module, cloud)

    version_record = datastore_version.find(datastore, version)

    if state == "absent":
        if version_record:
            datastore_version.delete(version_record["id"])
            module.exit_json(
                changed=True,
                msg="Successfully deleted version %s for datastore %s."
                % (version, datastore),
            )
        else:
            module.exit_json(
                changed=False,
                msg="Version %s for datastore %s does not exist."
                % (version, datastore),
            )
    else:
        if version_record:
            if datastore_version.update(version_record, state, image_tags, image_id):
                new_record = datastore_version.show(version_record["id"])
                module.exit_json(
                    changed=True,
                    msg="Version %s for datastore %s updated successfully."
                    % (version, datastore),
                    datastore_version=new_record,
                )
            else:
                module.exit_json(
                    changed=False,
                    msg="Version %s for datastore %s up to date."
                    % (version, datastore),
                    datastore_version=version_record,
                )
        else:
            version_record = datastore_version.create(
                manager, datastore, version, state, image_tags, image_id
            )
            cmd = [
                "trove-manage",
                "db_load_datastore_config_parameters",
                datastore,
                version,
                validation_rules,
            ]

            rc, out, err = module.run_command(cmd)
            if rc != 0:
                module.fail_json(msg="Error loading validation rules", out=out, err=err)

            module.exit_json(
                changed=True,
                msg="Version %s for datastore %s created successfully."
                % (version, datastore),
                datastore_version=version_record,
            )


if __name__ == "__main__":
    main()
