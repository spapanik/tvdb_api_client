<p align="center">
    <a href="https://github.com/ambv/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
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

The cache can be any object from a class that implements the get and set methods. The simplest solution would be the following:
```python
class C(dict):
    def set(self, key, value):
        self[key] = value

cache = C()
```

It is advisable to use a cache that will persist during a server restart, so that the token will not have to be regenerated. Please be advised that the token will be stored in the cache in plaintext, so if there are any security considerations they should be taken care into account when choosing the cache.

Once the client has been initialised, you can use it to get the following info (and the respective methods):

- Method to get TV series by TVDB id - `get_series_by_id(tvdb_id)`
- Method to get TV series by IMDb id - `get_series_by_imdb_id(imdb_id)`
- Method to find identifying info for a TV series by its name - `find_series_by_name(series_name)`
- Method to get episodes by TV series using its TVDB id - `get_episodes_by_series(tvdb_id)`

Note: the TVDB id can be an integer of a string in any method that it's required.
