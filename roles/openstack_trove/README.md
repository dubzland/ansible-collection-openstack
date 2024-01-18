# OpenStack Trove

Install and configure the OpenStack Trove DBaaS service.

## Requirements

This role is not meant to be used standalone, but instead should be used in
concert with the other roles in this collection. Specifically:

- The entire cluster must already be bootstrapped via the `openstack_bootstrap`
  role.
  OpenStack Keystone, Glance, Neutron, and Nova must already be installed and
  configured via their respective roles.
- The MySQL server must be available locally on the controller via unix socket.
- A `clouds.yaml` file must be available on the controller with proper admin
  credentials. This is automatically performed by the `openstack_bootstrap`
  role.

## Role Variables

Full documentation for the role is available in the [collection
documentation][1]. A minimum configuration needs to include the
following variables:

| Variable                                            | Comments                                                           |
| --------------------------------------------------- | ------------------------------------------------------------------ |
| `openstack_trove_db_password`                       | MySQL password to assign to the Trove database user.               |
| `openstack_trove_service_password`                  | Password to assign in Keystone for the Trove service.              |
| `openstack_trove_provider_network_name`             | Name of the Neutron provider network to create for DBaaS traffic.  |
| `openstack_trove_provider_network_type`             | Type of Neutron provider network to create.                        |
| `openstack_trove_provider_network_physical_network` | Underlying OVN network to attach the DBaaS provider network to.    |
| `openstack_trove_provider_network_segmentation_id`  | If `openstack_trove_provider_network_type` is `vlan`, the vlan id. |
| `openstack_trove_provider_network_network_ip`       | IP address of the controller on the DBaaS network.                 |
| `openstack_trove_provider_network_cidr`             | Network cidr to assign to the Neutron network for DBaaS.           |
| `openstack_trove_provider_network_allocation_pool`  | IP address pool to use for Trove instances on the DBaaS network.   |

## Usage

Install the collection locally, either via `requirements.yml`, or manually:

```console
ansible-galaxy collection install dubzland.openstack
```

Then apply the role using the following playbook:

```yaml
---
- hosts: openstack:&controller
  collections:
    - dubzland.openstack
  pre_tasks:
    - name: Assign the DBaaS management address
      ansible.builtin.set_fact:
        openstack_trove_provider_network_ip: >-
          {{ ansible_facts['ansible_' + lbaas_interface]['ipv4']['address'] }}
  roles:
    - role: openstack_trove
      vars:
        openstack_trove_db_password: supersekret
        openstack_trove_service_password: supersekret
        openstack_trove_provider_network_name: dbaas-mgmt
        openstack_trove_provider_physical_network: dbaas
        openstack_trove_provider_network_segmentation_id: 16
        openstack_trove_network_ip: 172.18.16.23
        openstack_trove_network_cidr: 172.18.16.0/24
        openstack_trove_network_allocation_pool:
          start: 172.18.16.150
          end: 172.18.16.254
  post_tasks:
    - name: Ensure the MySQL datastore version exists
      dubzland.openstack.openstack_datastore_version:
        cloud: local
        manager: mysql
        datastore: mysql
        version: "5.7.29"
        image_tags:
          - trove
          - mysql
        validation_rules: /usr/lib/python3/dist-packages/trove/templates/mysql/validation-rules.json
        state: enabled
```

## License

See [LICENSE](LICENSE).

## Author

- [Josh Williams](https://dubzland.com)

[1]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_trove_role.html
