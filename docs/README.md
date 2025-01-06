# tvdb_api_client: an unofficial API for the TVDB

[![build][build_badge]][build_url]
[![lint][lint_badge]][lint_url]
[![tests][tests_badge]][tests_url]
[![license][licence_badge]][licence_url]
[![codecov][codecov_badge]][codecov_url]
[![readthedocs][readthedocs_badge]][readthedocs_url]
[![pypi][pypi_badge]][pypi_url]
[![downloads][pepy_badge]][pepy_url]
[![code style: black][black_badge]][black_url]
[![build automation: yam][yam_badge]][yam_url]
[![Lint: ruff][ruff_badge]][ruff_url]

`tvdb_api_client` is an unofficial API for the TVDB.

## In a nutshell

### Installation

The easiest way is to use [poetry](https://python-poetry.org/) to manage
your dependencies and add _tvdb_api_client_ to them.

```toml
[tool.poetry.dependencies]
tvdb_api_client = "*"
```

### Usage

Initialise the client (example using the django cache):

```python
from django.core.cache import cache
from tvdb_api_client import TVDBClient

client = TVDBClient("username", "user_key", "api_key", cache)
```

Once the client has been initialised, you can use it to get the
following info:

-   get TV series by TVDB id
-   get TV series by IMDb id
-   find identifying info for a TV series by its name
-   get episodes by TV series using its TVDB id

## Links

-   [Documentation]
-   [Changelog]

[build_badge]: https://github.com/spapanik/tvdb_api_client/actions/workflows/build.yml/badge.svg
[build_url]: https://github.com/spapanik/tvdb_api_client/actions/workflows/build.yml
[lint_badge]: https://github.com/spapanik/tvdb_api_client/actions/workflows/lint.yml/badge.svg
[lint_url]: https://github.com/spapanik/tvdb_api_client/actions/workflows/lint.yml
[tests_badge]: https://github.com/spapanik/tvdb_api_client/actions/workflows/tests.yml/badge.svg
[tests_url]: https://github.com/spapanik/tvdb_api_client/actions/workflows/tests.yml
[licence_badge]: https://img.shields.io/pypi/l/tvdb-api-client
[licence_url]: https://tvdb-api-client.readthedocs.io/en/stable/LICENSE/
[codecov_badge]: https://codecov.io/github/spapanik/tvdb-api-client/graph/badge.svg?token=Q20F84BW72
[codecov_url]: https://codecov.io/github/spapanik/tvdb-api-client
[readthedocs_badge]: https://readthedocs.org/projects/tvdb-api-client/badge/?version=latest
[readthedocs_url]: https://tvdb-api-client.readthedocs.io/en/latest/
[pypi_badge]: https://img.shields.io/pypi/v/tvdb-api-client
[pypi_url]: https://pypi.org/project/tvdb-api-client
[pepy_badge]: https://pepy.tech/badge/tvdb-api-client
[pepy_url]: https://pepy.tech/project/tvdb-api-client
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black_url]: https://github.com/psf/black
[yam_badge]: https://img.shields.io/badge/build%20automation-yamk-success
[yam_url]: https://github.com/spapanik/yamk
[ruff_badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json
[ruff_url]: https://github.com/charliermarsh/ruff
[Documentation]: https://tvdb-api-client.readthedocs.io/en/stable/
[Changelog]: https://tvdb-api-client.readthedocs.io/en/stable/CHANGELOG/
