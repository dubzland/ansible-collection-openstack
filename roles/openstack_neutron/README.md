# Ansible Role: OpenStack Neutron

Install and configure the OpenStack Neutron networking services.

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
    - role: openstack_neutron
      vars:
        openstack_neutron_db_password: supersekret
        openstack_neutron_service_password: supersekret
        openstack_neutron_nova_service_password: supersekret
        openstack_neutron_nova_metadata_secret: supersekret
        openstack_neutron_ovn_tunnel_address: 172.18.82.51
        openstack_neutron_provider_networks:
          - name: external
            bridge: br-ex
            interface: enp7s19.134
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_neutron_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
