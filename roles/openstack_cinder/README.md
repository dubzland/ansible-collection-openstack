# Ansible Role: OpenStack Cinder

Install and configure the OpenStack Cinder block storage.

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
    - role: openstack_cinder
      vars:
        openstack_cinder_db_password: supersekret
        openstack_cinder_service_password: supersekret
        openstack_cinder_volume_types:
          - name: lvm
            description: iSCSI Block Device
            specs:
              volume_backend_name: LVM_iSCSI
              volume_driver: cinder.volume.drivers.lvm.LVMVolumeDriver
              volume_group: cinder-volumes
              target_protocol: iscsi
              target_helper: tgtadm
          - name: rbd
            description: Rados Block Device
            specs:
              volume_backend_name: RBD
              volume_driver: cinder.volume.drivers.rbd.RBDDriver
              rbd_ceph_conf: /etc/ceph/ceph.conf
              rbd_pool: volumes
              rbd_store_chunk_size: 8
              rbd_user: cinder
              report_discard_supported: true
          - name: __DEFAULT__
            state: absent
```

## Documentation

Role documentation is available at <https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_cinder_role.html>.

## License

MIT

## Author

- [Josh Williams](https://dubzland.com)
