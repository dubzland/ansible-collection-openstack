# Ansible Role: OpenStack Nova

Install and configure the OpenStack Nova compute component.

## Requirements

- Node must have been bootstrapped using the `openstack_bootstrap` role in this
  collection.
- OpenStack Keystone must already be installed and configured on the
  controller using the `openstack_keystone` role in this collection.
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
    - role: openstack_nova
      vars:
        openstack_nova_db_password: supersekret
        openstack_nova_service_password: supersekret
        openstack_nova_placement_service_password: supersekret
        openstack_nova_neutron_service_password: supersekret
        openstack_nova_neutron_metadata_secret: supersekret
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_nova_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
