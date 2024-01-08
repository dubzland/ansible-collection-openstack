# Ansible Role: OpenStack Horizon

Install and configure the OpenStack Horizon dashboard.

## Requirements

- Controller must have been bootstrapped using the `openstack_bootstrap` role
  in this collection.
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
    - role: openstack_horizon
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_horizon_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
