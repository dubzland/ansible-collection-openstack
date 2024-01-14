# OpenStack Neutron

Install and configure the OpenStack Neutron networking services.

## Requirements

This role is not meant to be used standalone, but instead should be used in
concert with the other roles in this collection. Specifically:

- The entire cluster must already be bootstrapped via the `openstack_bootstrap`
  role.
  OpenStack Keystone must already be installed and configured on the
  controller via the `openstack_keystone` role.
- The MySQL server must be available locally on the controller via unix socket.
- A `clouds.yaml` file must be available on the controller with proper admin
  credentials. This is automatically performed by the `openstack_bootstrap`
  role.

## Role Variables

Full documentation for the role is available in the [collection
documentation][1]. A minimum configuration needs to include the
following variables:

| Variable                                    | Comments                                                                                             |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| openstack_neutron_db_password               | MySQL password to assign to the Neutron database user.                                               |
| openstack_neutron_service_password          | Password to assign in Keystone for the Neutron service.                                              |
| openstack_neutron_nova_service_password     | Password configured for the Nova service in Keystone.                                                |
| openstack_neutron_nova_metadata_secret      | Random secret value shared between Neutron and Nova.                                                 |
| openstack_neutron_ovn_tunnel_address        | IP address on the tenant overlay network for compute nodes.                                          |
| openstack_neutron_provider_networks         | List of provider networks to be configured on the host (and in OVN). See the example playbook below. |
| openstack_neutron_provider_network_mappings | List of mappings from OVN networks to physical bridges/interfaces. See the example playbook below.   |

## Usage

Install the collection locally, either via `requirements.yml`, or manually:

```shell
ansible-galaxy collection install dubzland.openstack
```

Then apply the role using the following playbook:

```yaml
---
- hosts: compute:controller:&openstack
  collections:
    - dubzland.openstack
  vars:
    openstack_neutron_provider_networks:
      - name: provider
        type: vlan
  pre_tasks:
    - name: Assign the OVN tunnel address
      ansible.builtin.set_fact:
        openstack_neutron_ovn_tunnel_address: >-
          {{ ansible_facts['ansible_' + tunnel_interface]['ipv4']['address'] }}
      when: "'compute' in group_names"
    - name: Assign the provider network mappings
      ansible.builtin.set_fact:
        openstack_neutron_provider_network_mappings:
          - name: provider
            bridge: br-provider
            interface: bond0
      when: "'compute' in group_names"
  roles:
    - role: openstack_neutron
      vars:
        openstack_neutron_db_password: supersekret
        openstack_neutron_service_password: supersekret
        openstack_neutron_nova_service_password: supersekret
        openstack_neutron_nova_metadata_secret: supersekret
```

## License

See [LICENSE](LICENSE.md).

## Author

- [Josh Williams](https://dubzland.com)

[1]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_neutron_role.html
