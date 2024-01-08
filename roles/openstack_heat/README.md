# Ansible Role: OpenStack Heat

Install and configure the OpenStack Heat orchestration component.

## Requirements

- Node must have been bootstrapped using the `openstack_bootstrap` role in this
  collection.
- OpenStack Keystone, Nova, and Neutron must already be installed and configured
  via their corresponding roles in this collection.
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
    - role: openstack_heat
      vars:
        openstack_heat_db_password: supersekret
        openstack_heat_service_password: supersekret
        openstack_heat_domain_admin_password: supersekret
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_heat_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
