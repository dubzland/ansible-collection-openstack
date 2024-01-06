#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp

        # Create a backup of the original configuration file
        copy_task = self._task.copy()
        for remove in (
            "newline_sequence",
            "block_start_string",
            "block_end_string",
            "variable_start_string",
            "variable_end_string",
            "comment_start_string",
            "comment_end_string",
            "trim_blocks",
            "lstrip_blocks",
            "output_encoding",
        ):
            copy_task.args.pop(remove, None)

        dest = self._task.args["dest"]

        copy_task_args = {
            "src": dest,
            "dest": "%s.orig" % dest,
            "remote_src": True,
            "owner": "root",
            "group": "root",
            "force": False,
            "mode": "0660",
        }

        result.update(
            self._execute_module(
                module_name="copy", module_args=copy_task_args, task_vars=task_vars
            )
        )

        if result.get("failed"):
            return result

        # Execute the original template action
        template_action = self._shared_loader_obj.action_loader.get(
            "ansible.builtin.template",
            task=self._task,
            connection=self._connection,
            play_context=self._play_context,
            loader=self._loader,
            templar=self._templar,
            shared_loader_obj=self._shared_loader_obj,
        )
        result.update(template_action.run(task_vars=task_vars))

        return result
