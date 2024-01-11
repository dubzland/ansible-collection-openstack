# Ansible Role: OpenStack Ceph Client

Install and configure Ceph client on OpenStack nodes.

## Requirements

- Ceph cluster must already be provisioned, and client keyrings/pools added.

## Usage

Install the collection locally, either via `requirements.yml`, or manually:

```bash
ansible-galaxy collection install dubzland.openstack
```

Then apply the role using the following playbook:

```yaml
---
- hosts: compute:storage:&openstack

  collections:
    - dubzland.openstack

  roles:
    - role: openstack_ceph_client
      vars:
        openstack_ceph_client_bootstrap_host: 172.18.64.42
        openstack_ceph_client_keys:
          - cinder
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_ceph_client_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
