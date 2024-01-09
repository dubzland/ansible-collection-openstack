# Ansible Role: OpenStack Magnum

Install and configure the OpenStack Magnum container orchestration engine component.

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
    - role: openstack_magnum
      vars:
        openstack_magnum_db_password: supersekret
        openstack_magnum_service_password: supersekret
        openstack_magnum_domain_admin_password: supersekret
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_magnum_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
