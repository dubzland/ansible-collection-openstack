# Ansible Collection: OpenStack

[![Gitlab pipeline][pipeline-badge]][pipeline-url]
[![Gitlab coverage][coverage-badge]][coverage-url]
[![Galaxy Version][galaxy-badge]][galaxy-url]
[![license][license-badge]][license-url]
[![Liberapay patrons][liberapay-patrons-badge]][liberapay-url]
[![Liberapay receiving][liberapay-receives-badge]][liberapay-url]

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

| Name                                                              | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| [dubzland.openstack.openstack_barbican][openstack_barbican]       | Installs OpenStack Barbican key management                        |
| [dubzland.openstack.openstack_bootstrap][openstack_bootstrap]     | Prepares hosts for installing OpenStack components                |
| [dubzland.openstack.openstack_ceph_client][openstack_ceph_client] | Configuration related tasks for components requiring Ceph access  |
| [dubzland.openstack.openstack_cinder][openstack_cinder]           | Installs OpenStack Cinder block storage                           |
| [dubzland.openstack.openstack_component][openstack_component]     | Common component installation tasks                               |
| [dubzland.openstack.openstack_designate][openstack_designate]     | Installs OpenStack Designate DNSaaS                               |
| [dubzland.openstack.openstack_glance][openstack_glance]           | Installs OpenStack Glance image services                          |
| [dubzland.openstack.openstack_heat][openstack_heat]               | Installs OpenStack Heat orchestration services                    |
| [dubzland.openstack.openstack_horizon][openstack_horizon]         | Installs OpenStack Horizon dashboard                              |
| [dubzland.openstack.openstack_keystone][openstack_keystone]       | Installs OpenStack Keystone authentication                        |
| [dubzland.openstack.openstack_magnum][openstack_magnum]           | Installs OpenStack Magnum container orchestration engine services |
| [dubzland.openstack.openstack_neutron][openstack_neutron]         | Installs OpenStack Neutron networking services                    |
| [dubzland.openstack.openstack_nova][openstack_nova]               | Installs OpenStack Nova compute services                          |
| [dubzland.openstack.openstack_octavia][openstack_octavia]         | Installs OpenStack Octavia LBaaS services                         |
| [dubzland.openstack.openstack_placement][openstack_placement]     | Installs OpenStack Placement API                                  |
| [dubzland.openstack.openstack_swift][openstack_swift]             | Installs OpenStack Swift object store                             |
| [dubzland.openstack.openstack_trove][openstack_trove]             | Installs OpenStack Trove DBaaS                                    |

### Modules

| Name                                                                      | Description                                    |
| ------------------------------------------------------------------------- | ---------------------------------------------- |
| [dubzland.openstack.openstack_get_fact][openstack_get_fact]               | Retrieves facts stored as ansible custom facts |
| [dubzland.openstack.openstack_set_fact][openstack_set_fact]               | Stores facts in ansible custom facts           |
| [dubzland.openstack.openstack_config_template][openstack_config_template] | Templates configuration files with backup      |

## Licensing

This collection is primarily licensed and distributed as a whole under the MIT License.

See [LICENSE](https://git.dubzland.com/dubzland/ansible-collections/openstack/blob/main/LICENSE) for the full text.

## Author

- [Josh Williams](https://dubzland.com)

[pipeline-badge]: https://img.shields.io/gitlab/pipeline-status/dubzland%2Fansible-collections%2Fopenstack?gitlab_url=https%3A%2F%2Fgit.dubzland.com&branch=main&style=flat-square&logo=gitlab
[pipeline-url]: https://git.dubzland.com/dubzland/ansible-collections/openstack/pipelines?scope=all&page=1&ref=main
[coverage-badge]: https://img.shields.io/gitlab/pipeline-coverage/dubzland%2Fansible-collections%2Fopenstack?gitlab_url=https%3A%2F%2Fgit.dubzland.com&branch=main&style=flat-square&logo=gitlab
[coverage-url]: https://git.dubzland.com/dubzland/ansible-collections/openstack/pipelines?scope=all&page=1&ref=main
[galaxy-badge]: https://img.shields.io/badge/dynamic/json?style=flat-square&label=galaxy&prefix=v&url=https://galaxy.ansible.com/api/v3/collections/dubzland/openstack/&query=highest_version.version
[galaxy-url]: https://galaxy.ansible.com/ui/repo/published/dubzland/openstack/
[license-badge]: https://img.shields.io/gitlab/license/dubzland%2Fcontainer-images%2Fci-python?gitlab_url=https%3A%2F%2Fgit.dubzland.com&style=flat-square
[license-url]: https://git.dubzland.com/dubzland/container-images/ci-python/-/blob/main/LICENSE
[liberapay-patrons-badge]: https://img.shields.io/liberapay/patrons/jdubz?style=flat-square&logo=liberapay
[liberapay-receives-badge]: https://img.shields.io/liberapay/receives/jdubz?style=flat-square&logo=liberapay
[liberapay-url]: https://liberapay.com/jdubz/donate
[openstack_barbican]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_barbican_role.html
[openstack_bootstrap]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_bootstrap_role.html
[openstack_ceph_client]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_ceph_client_role.html
[openstack_cinder]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_cinder_role.html
[openstack_component]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_component_role.html
[openstack_designate]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_designate_role.html
[openstack_glance]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_glance_role.html
[openstack_heat]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_heat_role.html
[openstack_horizon]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_horizon_role.html
[openstack_keystone]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_keystone_role.html
[openstack_magnum]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_magnum_role.html
[openstack_neutron]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_neutron_role.html
[openstack_nova]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_nova_role.html
[openstack_octavia]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_octavia_role.html
[openstack_placement]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_placement_role.html
[openstack_swift]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_swift_role.html
[openstack_trove]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_trove_role.html
[openstack_get_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_get_fact_module.html
[openstack_set_fact]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_set_fact_module.html
[openstack_config_template]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_config_template_module.html
