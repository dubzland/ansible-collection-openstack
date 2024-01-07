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
        openstack_component_database_user: barbican
        openstack_component_database_password: supersekret
        openstack_component_databases:
          - barbican
        openstack_component_user: barbican
        openstack_component_password: supersekret
        openstack_component_services:
          - name: barbican
            type: key-manager
            description: OpenStack Key Management
            endpoints:
              - interface: public
                url: "http://{{ controller_fqdn }}:9311"
              - interface: internal
                url: "http://{{ controller_fqdn }}:9311"
              - interface: admin
                url: "http://{{ controller_fqdn }}:9311"
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_barbican_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
