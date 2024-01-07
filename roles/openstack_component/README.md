# Ansible Role: OpenStack component

Common tasks for registering and provisioning services and endpoints with an
OpenStack cloud. Designed to be applied to the controller node. Assumes the
MySQL server for the cluster is accessible via local socket at
`/run/mysqld/mysqld.sock`.

## Requirements

- OpenStack Keystone must already be installed and configured on the
  controller.
- A `clouds.yaml` file must be available with proper admin credentials.

## Usage

Install the collection locally, either via `requirements.yml`, or manually:

```bash
ansible-galaxy collection install dubzland.openstack
```

Then apply the role using the following playbook:

```yaml
---
- hosts: openstack:&controller

  collections:
    - dubzland.openstack

  roles:
    - role: openstack_component
      vars:
        openstack_component_database_user: cinder
        openstack_component_database_password: supersekret
        openstack_component_databases:
          - cinder
        openstack_component_user: cinder
        openstack_component_password: supersekret
        openstack_component_services:
          - name: cinderv3
            type: volumev3
            description: OpenStack Block Storage
            endpoints:
              - interface: public
                url: "http://{{ controller_fqdn }}:8776/v3/%(project_id)s"
              - interface: internal
                url: "http://{{ controller_fqdn }}:8776/v3/%(project_id)s"
              - interface: admin
                url: "http://{{ controller_fqdn }}:8776/v3/%(project_id)s"
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_common_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
