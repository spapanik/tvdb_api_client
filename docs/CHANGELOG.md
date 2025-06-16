# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

## [0.7.0] - 2025-02-01

### Added

- Added python 3.11 support
- Added python 3.12 support
- Added python 3.13 support

### Removed

- Dropped support for TVDB APIv3
- Drop python 3.7 support
- Drop python 3.8 support

### Changed

- The API Key and PIN can now be passed as env vars or from a file

## [0.6.0] - 2022-03-08

### Added

- Added a method to get series by the tvdb id (V4 API)
- Added a method to get all episodes from a series by the tvdb id of
  the series (V4 API)

### Removed

- Removed changelog from the published wheel

## [0.5.0] - 2022-01-05

### Added

- Added python310 support

### Removed

- Dropped python36 support

## [0.4.2] - 2021-02-14

### Added

- Allow setting the language

## [0.4.1] - 2020-09-30

### Fixed

- Add method get_episodes_by_series back to the class

## [0.4.0] - 2020-04-23

### Added

- Add caching to all methods

## [0.3.0] - 2020-01-25

### Added

- Dummy cache when no cache specified

## [0.2.0] - 2019-05-27

### Added

- changelog.md
- Method to get TV series by TVDB id
- Method to get TV series by IMDb id
- Method to find identifying info for a TV series by its name
- Method to get episodes by TV series using its TVDB id

## [0.1.7] - 2019-05-20

### Added

## [0.1.6] - 2018-10-06

### Added

## [0.1.5] - 2018-10-06

### Added

## [0.1.3] - 2018-10-06

### Added

## [0.1.2] - 2018-10-06

### Added

## [0.1.0] - 2018-02-24

### Added

## [0.0.2] - 2017-08-06

### Added

## [0.0.1] - 2017-08-05

### Added

[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[Unreleased]: https://github.com/spapanik/tvdb_api_client/compare/v0.7.0...master
[0.7.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.4.2...v0.5.0
[0.4.2]: https://github.com/spapanik/tvdb_api_client/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/spapanik/tvdb_api_client/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.1.7...v0.2.0
[0.1.7]: https://github.com/spapanik/tvdb_api_client/compare/v0.1.6...v0.1.7
[0.1.6]: https://github.com/spapanik/tvdb_api_client/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/spapanik/tvdb_api_client/compare/v0.1.3...v0.1.5
[0.1.3]: https://github.com/spapanik/tvdb_api_client/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/spapanik/tvdb_api_client/compare/v0.1.0...v0.1.2
[0.1.0]: https://github.com/spapanik/tvdb_api_client/compare/v0.0.2...v0.1.0
[0.0.2]: https://github.com/spapanik/tvdb_api_client/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/spapanik/tvdb_api_client/releases/tag/v0.0.1
