===============================================
tvdb_api_client: an unofficial API for the TVDB
===============================================

.. image:: https://github.com/spapanik/tvdb_api_client/actions/workflows/build.yml/badge.svg
  :alt: Build
  :target: https://github.com/spapanik/tvdb_api_client/actions/workflows/build.yml
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

Once the client has been initialised, you can use it to get the following info:

* get TV series by TVDB id
* get TV series by IMDb id
* find identifying info for a TV series by its name
* get episodes by TV series using its TVDB id

Links
-----

- `Documentation`_
- `Changelog`_


.. _poetry: https://python-poetry.org/
.. _Changelog: https://github.com/spapanik/tvdb_api_client/blob/main/CHANGELOG.rst
.. _Documentation: https://tvdb-api-client.readthedocs.io/en/latest/
