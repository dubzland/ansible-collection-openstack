# Ansible Role: OpenStack Octavia

Install and configure the OpenStack Octavia LBaaS component.

## Requirements

- Controller must have been bootstrapped using the `openstack_bootstrap` role
  in this collection.
- OpenStack Keystone, Neutron, and Nova, and Barbican must already be installed
  and configured using their respective roles in this collection.
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
    - role: openstack_octavia
      vars:
        openstack_octavia_db_password: supersekret
        openstack_octavia_service_password: supersekret
        openstack_octavia_amphora_public_key: <SSH public key>
        openstack_octavia_heartbeat_key: <Key data>
        openstack_octavia_provider_network_name: lbaas-mgmt
        openstack_octavia_provider_physical_network: lbaas
        openstack_octavia_network_ip: 172.18.98.23
        openstack_octavia_network_cidr: 172.18.98.0/24
        openstack_octavia_network_allocation_pool:
          start: 172.18.99.150
          end: 172.18.98.254
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_octavia_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
