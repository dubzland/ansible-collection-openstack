# OpenStack Designate

Install and configure the OpenStack Designate DNSaaS component.

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

| Variable                             | Comments                                                                   |
| ------------------------------------ | -------------------------------------------------------------------------- |
| openstack_designate_db_password      | MySQL password to assign to the Designate database user.                   |
| openstack_designate_service_password | Password to assign in Keystone for the Designate service.                  |
| openstack_designate_rndc_keys        | List of TSIG keys to be installed on the controller.                       |
| openstack_designate_pools            | List of upstream DNS servers to configure. See the example playbook below. |

## Usage

Install the collection locally, either via `requirements.yml`, or manually:

```shell
ansible-galaxy collection install dubzland.openstack
```

Then apply the role using the following playbook:

```yaml
---
- hosts: openstack:&controller
  collections:
    - dubzland.openstack
  roles:
    - role: openstack_designate
      vars:
        openstack_designate_db_password: supersekret
        openstack_designate_service_password: supersekret
        openstack_designate_rndc_keys:
          - name: designate
            algorithm: hmac-sha512
            secret: <rndc key secret>
        openstack_designate_pools:
          - description: Default BIND9 Pool
            name: default
            nameservers:
              - host: 172.18.9.53
            ns_records:
              - hostname: os-dns.example.com
            targets:
              - description: Default Bind9 Pool
                type: bind9
                masters:
                  - host: "{{ ansible_default_ipv4['address'] }}"
                options:
                  host: 172.18.9.53
                  rndc_host: 172.18.9.53
                  rndc_key_file: /etc/designate/rndc.key
```

## License

See [LICENSE](LICENSE.md).

## Author

- [Josh Williams](https://dubzland.com)

[1]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_designate_role.html
