# Ansible Collection: OpenStack

[![Gitlab pipeline status (self-hosted)](https://git.dubzland.com/dubzland/ansible-collection-openstack/badges/main/pipeline.svg)](https://git.dubzland.com/dubzland/ansible-collection-openstack/pipelines?scope=all&page=1&ref=main)
[![Ansible Galaxy](https://img.shields.io/badge/dynamic/json?style=flat&label=galaxy&prefix=v&url=https://galaxy.ansible.com/api/v3/collections/dubzland/openstack/&query=highest_version.version)](https://galaxy.ansible.com/ui/repo/published/dubzland/openstack/)
[![Liberapay patrons](https://img.shields.io/liberapay/patrons/jdubz)](https://liberapay.com/jdubz/donate)
[![Liberapay receiving](https://img.shields.io/liberapay/receives/jdubz)](https://liberapay.com/jdubz/donate)

Installs and configures various components of the OpenStack cloud computing
platform.

## Ansible version compatibility

This collection has been tested against following ansible-core versions:

- 2.13
- 2.14
- 2.15
- 2.16

Also tested against the current development version of `ansible-core`.

## Included content

### Roles

| Name                                                              | Description                                                      |
| ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| [dubzland.openstack.openstack_barbican][openstack_barbican]       | Installs OpenStack Barbican key management                       |
| [dubzland.openstack.openstack_bootstrap][openstack_bootstrap]     | Prepares hosts for installing OpenStack components               |
| [dubzland.openstack.openstack_ceph_client][openstack_ceph_client] | Configuration related tasks for components requiring Ceph access |
| [dubzland.openstack.openstack_cinder][openstack_cinder]           | Installs OpenStack Cinder block storage                          |
| [dubzland.openstack.openstack_component][openstack_component]     | Common component installation tasks                              |
| [dubzland.openstack.openstack_glance][openstack_glance]           | Installs OpenStack Glance image services                         |
| [dubzland.openstack.openstack_keystone][openstack_keystone]       | Installs OpenStack Keystone authentication                       |
| [dubzland.openstack.openstack_neutron][openstack_neutron]         | Installs OpenStack Neutron networking services                   |
| [dubzland.openstack.openstack_nova][openstack_nova]               | Installs OpenStack Nova compute services                         |
| [dubzland.openstack.openstack_placement][openstack_placement]     | Installs OpenStack Placement API                                 |

### Modules

| Name                                                                      | Description                                    |
| ------------------------------------------------------------------------- | ---------------------------------------------- |
| [dubzland.openstack.openstack_get_fact][openstack_get_fact]               | Retrieves facts stored as ansible custom facts |
| [dubzland.openstack.openstack_set_fact][openstack_set_fact]               | Stores facts in ansible custom facts           |
| [dubzland.openstack.openstack_config_template][openstack_config_template] | Templates configuration files with backup      |

## Licensing

This collection is primarily licensed and distributed as a whole under the MIT License.

See [LICENSE](https://git.dubzland.com/dubzland/ansible-collection-openstack/blob/main/LICENSE) for the full text.

## Author

- [Josh Williams](https://dubzland.com)

[openstack_barbican]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_barbican_role.html
[openstack_bootstrap]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_bootstrap_role.html
[openstack_ceph_client]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_ceph_client_role.html
[openstack_cinder]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_cinder_role.html
[openstack_component]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_component_role.html
[openstack_glance]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_glance_role.html
[openstack_keystone]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_keystone_role.html
[openstack_neutron]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_neutron_role.html
[openstack_nova]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_nova_role.html
[openstack_placement]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_placement_role.html
[openstack_get_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_get_fact_module.html
[openstack_set_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_set_fact_module.html
[openstack_config_template]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_config_template_module.html
