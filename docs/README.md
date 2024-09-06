# tvdb_api_client: an unofficial API for the TVDB

[![tests][test_badge]][test_url]
[![license][licence_badge]][licence_url]
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

[test_badge]: https://github.com/spapanik/tvdb_api_client/actions/workflows/tests.yml/badge.svg
[test_url]: https://github.com/spapanik/tvdb_api_client/actions/workflows/tests.yml
[licence_badge]: https://img.shields.io/pypi/l/tvdb-api-client
[licence_url]: https://github.com/spapanik/tvdb_api_client/blob/main/docs/LICENSE.md
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
[Changelog]: https://github.com/spapanik/tvdb_api_client/blob/main/docs/CHANGELOG.md
