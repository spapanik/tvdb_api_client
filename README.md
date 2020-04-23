<p align="center">
<a href="https://travis-ci.org/spapanik/tvdb_api_client"><img alt="Build" src="https://travis-ci.org/spapanik/tvdb_api_client.svg?branch=master"></a>
<a href="https://coveralls.io/github/spapanik/tvdb_api_client"><img alt="Coverage" src="https://coveralls.io/repos/github/spapanik/tvdb_api_client/badge.svg?branch=master"></a>
<a href="https://github.com/spapanik/tvdb_api_client/blob/master/LICENSE.txt"><img alt="License" src="https://img.shields.io/github/license/spapanik/tvdb_api_client"></a>
<a href="https://pypi.org/project/tvdb_api_client"><img alt="PyPI" src="https://img.shields.io/pypi/v/tvdb_api_client"></a>
<a href="https://pepy.tech/project/tvdb-api-client"><img alt="Downloads" src="https://pepy.tech/badge/tvdb-api-client"></a>
<a href="https://github.com/psf/black"><img alt="Code style" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

A python client for the <a href="https://api.thetvdb.com/swagger#/">API</a> exposed by <a href="https://api.thetvdb.com/swagger#/">the TVDB</a>. API keys should be acquired from the TVDB site prior to using this client.

### Installation

tvdb_api_client can be installed by running `pip install tvdb_api_client`.  It requires Python 3.6+.

### Usage

Initialise the client (example using the django cache):
```python
from django.core.cache import cache
from tvdb_api_client import TVDBClient

client = TVDBClient("username", "user_key", "api_key", cache)
```

The cache can be any object from a class that implements the get and set methods. For convenience, you can pass only the other arguments, and a simple object that has them will be initialised.
```python
from tvdb_api_client import TVDBClient

client = TVDBClient("username", "user_key", "api_key")
```

It is advisable to use a cache that will persist during a server restart, so that the token will not have to be regenerated. Please be advised that the token will be stored in the cache in plaintext, so if there are any security considerations they should be taken care into account when choosing the cache.

Once the client has been initialised, you can use it to get the following info (and the respective methods):

- Method to get TV series by TVDB id - `get_series_by_id(tvdb_id)`
- Method to get TV series by IMDb id - `get_series_by_imdb_id(imdb_id)`
- Method to find identifying info for a TV series by its name - `find_series_by_name(series_name)`
- Method to get episodes by TV series using its TVDB id - `get_episodes_by_series(tvdb_id)`

Note: the TVDB id can be an integer of a string in any method that it's required. Also, all of these methods will used the cached value if present. To get new data, you may pass `refresh_cache=True` to all of them.
