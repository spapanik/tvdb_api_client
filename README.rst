===============================================
tvdb_api_client: an unofficial API for the TVDB
===============================================

.. image:: https://github.com/spapanik/tvdb_api_client/actions/workflows/build.yml/badge.svg
  :alt: Build
  :target: https://github.com/spapanik/tvdb_api_client/actions/workflows/build.yml
.. image:: https://img.shields.io/lgtm/alerts/g/spapanik/tvdb_api_client.svg
  :alt: Total alerts
  :target: https://lgtm.com/projects/g/spapanik/tvdb_api_client/alerts/
.. image:: https://img.shields.io/github/license/spapanik/tvdb_api_client
  :alt: License
  :target: https://github.com/spapanik/tvdb_api_client/blob/main/LICENSE.txt
.. image:: https://img.shields.io/pypi/v/tvdb_api_client
  :alt: PyPI
  :target: https://pypi.org/project/tvdb_api_client
.. image:: https://pepy.tech/badge/tvdb-api-client
  :alt: Downloads
  :target: https://pepy.tech/project/tvdb-api-client
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :alt: Code style
  :target: https://github.com/psf/black

``tvdb_api_client`` is an unofficial API for the TVDB.

In a nutshell
-------------

Installation
^^^^^^^^^^^^

The easiest way is to use `poetry`_ to manage your dependencies and add *tvdb_api_client* to them.

.. code-block:: toml

    [tool.poetry.dependencies]
    tvdb_api_client = "*"

Usage
^^^^^

Initialise the client (example using the django cache):

.. code:: python

    from django.core.cache import cache
    from tvdb_api_client import TVDBClient

    client = TVDBClient("username", "user_key", "api_key", cache)


The cache can be any object from a class that implements the get and set methods. For convenience, you can pass only the other arguments, and a simple object that has them will be initialised.

.. code:: python

    from tvdb_api_client import TVDBClient

    client = TVDBClient("username", "user_key", "api_key")

It is advisable to use a cache that will persist during a server restart, so that the token will not have to be regenerated. Please be advised that the token will be stored in the cache in plaintext, so if there are any security considerations they should be taken care into account when choosing the cache.

Once the client has been initialised, you can use it to get the following info (and the respective methods):

* Method to get TV series by TVDB id - ``get_series_by_id(tvdb_id)``
* Method to get TV series by IMDb id - ``get_series_by_imdb_id(imdb_id)``
* Method to find identifying info for a TV series by its name - ``find_series_by_name(series_name)``
* Method to get episodes by TV series using its TVDB id - ``get_episodes_by_series(tvdb_id)``

Note: the TVDB id can be an integer of a string in any method that it's required. Also, all of these methods will used the cached value if present. To get new data, you may pass ``refresh_cache=True`` to all of them.

Links
-----

- `Documentation`_
- `Changelog`_


.. _poetry: https://python-poetry.org/
.. _Changelog: https://github.com/spapanik/tvdb_api_client/blob/main/CHANGELOG.rst
.. _Documentation: https://tvdb-api-client.readthedocs.io/en/latest/
