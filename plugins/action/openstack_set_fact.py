#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# MIT License (see LICENSE or https://opensource.org/license/mit/)
# SPDX-License-Identifier: MIT

from __future__ import annotations

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp

        section = self._task.args["section"]
        option = self._task.args["option"]
        value = self._task.args["value"]
        dest = "/etc/ansible/facts.d/openstack.fact"
        owner = "root"
        group = "root"
        mode = "0640"

        ini_task_args = {
            "dest": dest,
            "section": section,
            "option": option,
            "value": value,
            "owner": owner,
            "group": group,
            "mode": mode,
        }

        result.update(
            self._execute_module(
                module_name="community.general.ini_file",
                module_args=ini_task_args,
                task_vars=task_vars,
            )
        )

        return result
