#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: openstack_set_fact
short_description: Records a local fact about the OpenStack configuration.
description:
  - Uses the M(community.general.ini_file) module to store facts locally.
  - Stores the facts in C(/etc/ansible/facts.d/openstack.fact).
  - Fact file will be owned by user and group C(root), with mode C(0640).
author:
    - Josh Williams (@t3hpr1m3)
requirements:
  - python >= 3.8
seealso:
- module: community.general.ini_file
options:
  section:
    type: str
    required: true
    description: Section within the OpenStack facts file to store this fact.
  option:
    type: str
    required: true
    description: Name of the fact being stored.
  value:
    type: str
    required: true
    description: Actual fact being stored.
"""

EXAMPLES = """
- name: Record the OpenStack version
  dubzland.openstack.openstack_set_fact:
    section: repository
    option: codename
    value: antelope
"""
