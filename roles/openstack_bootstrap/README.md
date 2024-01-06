# Ansible Role: OpenStack Bootstrap

Prepares hosts for installing OpenStack components

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
    - openstack_bootstrap
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_bootstrap_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
