# Ansible Role: OpenStack Glance

Install and configure the OpenStack Glance image management services.

## Requirements

- OpenStack Keystone must already be installed and configured on the
  controller.
- MySQL server available locally via unix socket.
- A `clouds.yaml` file must be available with proper admin credentials.

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
    - role: openstack_glance
      vars:
        openstack_glance_db_password: supersekret
        openstack_glance_service_password: supersekret
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_glance_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
