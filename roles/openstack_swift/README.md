# Ansible Role: OpenStack Swift

Install and configure the OpenStack Swift object storage component.

## Requirements

- Controller must have been bootstrapped using the `openstack_bootstrap` role
  in this collection.
- OpenStack Keystone, Neutron, and Nova, Barbican, and Heat must already be
  installed and configured using their respective roles in this collection.
- MySQL server available locally on the controller via unix socket.

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
    - role: openstack_swift
      vars:
        openstack_swift_service_password: supersekret
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_swift_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
