#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Josh Williams <jdubz@dubzland.com>
# MIT License (see LICENSE or https://opensource.org/license/mit/)
# SPDX-License-Identifier: MIT

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: openstack_get_fact
short_description: Retrieves a fact from local OpenStack facts.
description:
  - Reads the fact from variables in C(hostvars['ansible_local']), so be sure
    facts are already gathered.
  - Uses the M(ansible.builtin.set_fact) module to actually assign the fact.
author:
    - Josh Williams (@t3hpr1m3)
requirements:
  - python >= 3.8
seealso:
- module: ansible.builtin.set_fact
options:
  section:
    type: str
    required: true
    description: Section within the OpenStack facts file where fact is stored.
  option:
    type: str
    required: true
    description: Name of the fact being retrieved.
  as:
    type: str
    required: true
    description: Variable to be set with the fact value.
"""

EXAMPLES = """
- name: Retrieve the OpenStack version
  dubzland.openstack.openstack_get_fact:
    section: repository
    option: codename
    as: _openstack_version
"""
