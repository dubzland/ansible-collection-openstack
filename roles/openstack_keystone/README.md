# Ansible Role: OpenStack Keystone

Install and configure the OpenStack Keystone authentication service. This role
assumes all target machines have been bootstrapped via the `openstack_bootstrap`
role in this collection. Further, it is assumed that MySQL, Redis, and Memcache
have already been installed and configured according to the official OpenStack
documentation.

## Usage

Install the collection locally, either via `requirements.yml`, or manually:

```bash
ansible-galaxy collection install dubzland.openstack
```

Then apply the role using the following playbook:

```yaml
---
- hosts: openstack

  collections:
    - dubzland.openstack

  roles:
    - role: openstack_keystone
      vars:
        openstack_keystone_db_password: supersekret
        openstack_keystone_admin_password: supersekret
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_keystone_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
