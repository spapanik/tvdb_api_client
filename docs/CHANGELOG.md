# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

### Fixed

- Fixed missing episodes after the first 500 ones

### Removed

- Removed support for Python 3.9

### Security

- Updated `requests` to fix a security vulnerability (versions <2.32.4 were affected)

## [0.7.0] - 2025-02-01

### Added

- Added support for Python 3.11
- Added support for Python 3.12
- Added support for Python 3.13
- Exposed the `get` method for direct API access

### Changed

- The API key and PIN can now be passed as environment variables or from a file
- Changed the license to BSD 3-Clause

### Removed

- Removed support for TVDB API v3
- Removed support for Python 3.7
- Removed support for Python 3.8

## [0.6.0] - 2022-03-08

### Added

- Added `TVDBClientV4` with methods to get series and episodes using the V4 API
- Added `Series` and `Episode` dataclasses for V4 API responses

### Removed

- Removed the changelog from the published wheel

## [0.5.0] - 2022-01-05

### Added

- Added support for Python 3.10
- Added type annotations to the public API
- Added `py.typed` marker for PEP 561 compatibility

### Removed

- Removed support for Python 3.6

## [0.4.2] - 2021-02-14

### Added

- Added support for setting the language

## [0.4.1] - 2020-09-30

### Fixed

- Fixed a bug in `get_episodes_by_series`

### Changed

- Changed the license to LGPLv3

## [0.4.0] - 2020-04-23

### Added

- Added caching to all public methods
- Added a `refresh_cache` parameter to all public methods to force cache invalidation

## [0.3.0] - 2020-01-25

### Added

- Added a dummy cache when no cache is specified

## [0.2.0] - 2019-05-27

### Changed

- Renamed `get_tvdb_id` to `get_series_by_id`
- Renamed `get_imdb_id` to `get_series_by_imdb_id`
- Renamed `get_episodes` to `get_episodes_by_series`
- Removed the ability to set the name via the secrets file

## [0.1.7] - 2019-05-20

Maintenance release, no user-facing changes.

## [0.1.6] - 2018-10-06

Maintenance release, no user-facing changes.

## [0.1.5] - 2018-10-06

Maintenance release, no user-facing changes.

## [0.1.3] - 2018-10-06

Maintenance release, no user-facing changes.

## [0.1.2] - 2018-10-06

### Changed

- Set Python 3.6 as the minimum required Python version

## [0.1.0] - 2018-02-24

### Added

- Added support for storing API credentials in a file

### Changed

- Changed the client initialization to use keyword arguments

## [0.0.2] - 2017-08-06

Maintenance release, no user-facing changes.

## [0.0.1] - 2017-08-05

### Added

- Initial release with `TVDBClient` featuring methods to get a series by TVDB ID,
  get a series by IMDb ID, find identifying info for a series by name, and get
  episodes for a series

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
