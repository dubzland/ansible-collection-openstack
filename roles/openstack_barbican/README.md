# Ansible Role: OpenStack Barbican

Install and configure the OpenStack Barbican key management component.

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
    - role: openstack_barbican
      vars:
        openstack_barbican_db_password: supersekret
        openstack_barbican_service_password: supersekret
        openstack_barbican_crypto_key: YWYzODZhNzQ2OWI2OWYxMDE5MGNlY2UzY2Q4Njc0M2I=
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_barbican_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
