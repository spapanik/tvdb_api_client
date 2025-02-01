# Usage

The central object is the `TheTVDBClient` client which needs the
`api_key` supplied by the [TheTVDB]. It can be initialised with a
ache (optionally), and if no cache is passed a dummy cache object
will be created.

???+ tip "Cache"

    It is advisable to use a cache that will persist during a server
    restart, so that the token will not have to be regenerated.

!!! danger "Security warning"

    Please be advised that the token will be stored in the default
    cache in plaintext, so if there are any security considerations
    they should be taken care into account when choosing the cache.

## The TVDB API Client

The TVDB API Client is a class that offers the following public
methods:

-   get
-   get_raw_series_by_id
-   get_series_by_id
-   get_raw_episodes_by_series
-   get_episodes_by_series

???+ tip "Refreshing cache"

    Also, all of these methods will used the cached value if present.
    To get new data, you may pass `refresh_cache=True` to all of them.

You can initialise the class either by passing the api_key to the
class, or by setting it as the env var `TVDB_API_KEY_V4`, or by
creating a file called `the_tvdb.yaml` on `$XDG_CONFIG_HOME`.

!!! danger "Security warning"

    Passing secrets in env vars is insecure, as some operating systems
    allow non-root users to see process environment variables via ps.
    It is advised use the file option, and set the correct
    permissions to it.

[TheTVDB]: https://thetvdb.com/api-information
