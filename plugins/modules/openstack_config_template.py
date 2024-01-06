#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: openstack_config_template
short_description: Wrapper around templating, with backup of original
description:
  - Creates a backup of original configuration file (if present)
  - Applies the specified template using standard Ansible templating
author:
    - Josh Williams (@t3hpr1m3)
requirements:
  - python >= 3.8
seealso:
- module: ansible.builtin.copy
- module: ansible.builtin.template
extends_documentation_fragment:
- action_common_attributes
- action_common_attributes.flow
- action_common_attributes.files
- backup
- files
- validate
"""

EXAMPLES = """
- name: Apply Keystone configuration
  dubzland.openstack.openstack_config_template:
    src: etc/keystone/keystone.conf.j2
    dest: /etc/keystone/keystone.conf
    owner: keystone
    group: keystone
    mode: "0640"
  notify: Restart apache2
"""
