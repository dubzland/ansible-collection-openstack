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

| Name                                                          | Description                                        |
| ------------------------------------------------------------- | -------------------------------------------------- |
| [dubzland.openstack.openstack_bootstrap][openstack_bootstrap] | Prepares hosts for installing OpenStack components |

## Licensing

This collection is primarily licensed and distributed as a whole under the GNU General Public License v3.0 or later.

See [LICENSE](https://git.dubzland.com/dubzland/ansible-collection-minio/blob/main/LICENSE) for the full text.

## Author

- [Josh Williams](https://dubzland.com)

[openstack_bootstrap]: https://docs.dubzland.io/ansible-collections/collections/dubzland/openstack/openstack_bootstrap_role.html
