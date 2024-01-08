# Ansible Role: OpenStack Designate

Install and configure the OpenStack Designate DNSaaS component.

## Requirements

- Controller must have been bootstrapped using the `openstack_bootstrap` role
  in this collection.
- OpenStack Keystone must already be installed and configured on the
  controller using the `openstack_keystone` role in this collection.
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
    - role: openstack_designate
      vars:
        openstack_designate_db_password: supersekret
        openstack_designate_service_password: supersekret
        openstack_designate_rndc_key:
          name: designate
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

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_designate_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
