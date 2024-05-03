# Usage

The central object is the `TVDBClient` client which needs the
`username`, `user_key`, and `api_key` supplied by the TVDB. It can be
initialised with a cache (optionally), and if no cache is passed a dummy
cache object will be created.

::: note
::: title
Note
:::

It is advisable to use a cache that will persist during a server
restart, so that the token will not have to be regenerated.
:::

::: warning
::: title
Warning
:::

Please be advised that the token will be stored in the default cache in
plaintext, so if there are any security considerations they should be
taken care into account when choosing the cache.
:::

> The TVDB client

::: note
::: title
Note
:::

Also, all of these methods will used the cached value if present. To get
new data, you may pass `refresh_cache=True` to all of them.
:::
