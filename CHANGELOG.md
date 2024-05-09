# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Project now uses ci-templates for testing (#18)
- Move repository to `dubzland/ansible-collections/openstack` (#17)

## [1.1.0] - 2024-01-17

### Added

- Add the ability to configure vlan type provider networks in Neutron
- OpenStack Trove role
- OpenStack datastore version module

### Changed

- Multiple rndc keys can now be provided, allowing for different backends.
- Attributes can now be specified for pools, allowing for public/private pools.

## [1.0.0] - 2024-01-11

### Added

- OpenStack bootstrap role
- Configuration template module
- Local fact modules
- OpenStack Keystone role
- OpenStack Barbican role
- OpenStack Placement role
- OpenStack Glance role
- Ceph client role
- OpenStack Cinder role
- OpenStack Neutron role
- OpenStack Nova role
- OpenStack Heat role
- OpenStack Designate role
- OpenStack Horizon role
- OpenStack Octavia role
- OpenStack Magnum role
- OpenStack Swift role

[unreleased]: https://git.dubzland.com/dubzland/ansible-collections/openstack/-/compare/v1.1.0...HEAD
[1.1.0]: https://git.dubzland.com/dubzland/ansible-collections/openstack/-/compare/v1.0.0...v1.1.0
[1.0.0]: https://git.dubzland.com/dubzland/ansible-collections/openstack/-/tree/v1.0.0
