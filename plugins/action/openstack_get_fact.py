#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# MIT License (see LICENSE or https://opensource.org/license/mit/)
# SPDX-License-Identifier: MIT

from __future__ import annotations

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def get_value(self, section, option, vars):
        if "ansible_local" not in vars:
            raise AnsibleActionFail("'ansible_local' not populated")

        ansible_local = vars["ansible_local"]

        if "openstack" not in ansible_local:
            raise AnsibleActionFail(
                "OpenStack vars not set in ansible_local. Did you gather facts?"
            )

        openstack_facts = ansible_local["openstack"]

        keys = [section, option]
        _element = openstack_facts
        for key in keys:
            if key in _element:
                _element = _element[key]
            else:
                raise AnsibleActionFail(
                    "Unable to find OpenStack fact: %s -> %s" % (section, option)
                )

        return _element

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp

        section = self._task.args["section"]
        option = self._task.args["option"]
        fact_name = self._task.args["as"]
        new_task = self._task.copy()

        new_task.args = dict()
        new_task.args[fact_name] = self.get_value(section, option, task_vars)

        # Execute the builtin set_fact
        set_fact_action = self._shared_loader_obj.action_loader.get(
            "ansible.builtin.set_fact",
            task=new_task,
            connection=self._connection,
            play_context=self._play_context,
            loader=self._loader,
            templar=self._templar,
            shared_loader_obj=self._shared_loader_obj,
        )

        result.update(set_fact_action.run(task_vars=task_vars))

        return result
