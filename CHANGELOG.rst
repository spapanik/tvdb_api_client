=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_, and this project adheres to `Semantic Versioning`_.

`Unreleased`_
-------------

Removed
^^^^^^^
* Dropped support for TVDB APIv3
* Drop python 3.7 support

`0.6.0`_ - 2022-03-08
---------------------

Added
^^^^^
* Added a method to get series by the tvdb id (V4 API)
* Added a method to get all episodes from a series by the tvdb id of the series (V4 API)

Removed
^^^^^^^
* Removed changelog from the published wheel

`0.5.0`_ - 2022-01-05
---------------------

Added
^^^^^
* Added python310 support

Removed
^^^^^^^
* Dropped python36 support

`0.4.2`_ - 2021-02-14
---------------------

Added
^^^^^
* Allow setting the language

`0.4.1`_ - 2020-09-30
---------------------

Fixed
^^^^^
* Add method get_episodes_by_series back to the class

`0.4.0`_ - 2020-04-23
---------------------

Added
^^^^^
* Add caching to all methods

`0.3.0`_ - 2020-01-25
---------------------

Added
^^^^^
* Dummy cache when no cache specified

`0.2.0`_ - 2019-05-27
---------------------

Added
^^^^^
* changelog.md
* Method to get TV series by TVDB id
* Method to get TV series by IMDb id
* Method to find identifying info for a TV series by its name
* Method to get episodes by TV series using its TVDB id

`0.1.7`_ - 2019-05-20
---------------------

Added
^^^^^

`0.1.6`_ - 2018-10-06
---------------------

Added
^^^^^

`0.1.5`_ - 2018-10-06
---------------------

Added
^^^^^

`0.1.3`_ - 2018-10-06
---------------------

Added
^^^^^

`0.1.2`_ - 2018-10-06
---------------------

Added
^^^^^

`0.1.0`_ - 2018-02-24
---------------------

Added
^^^^^

`0.0.2`_ - 2017-08-06
---------------------

Added
^^^^^

`0.0.1`_ - 2017-08-05
---------------------

Added
^^^^^


.. _`unreleased`: https://github.com/spapanik/tvdb_api_client/compare/v0.6.0...master
.. _`0.6.0`: https://github.com/spapanik/tvdb_api_client/compare/v0.5.0...v0.6.0
.. _`0.5.0`: https://github.com/spapanik/tvdb_api_client/compare/v0.4.2...v0.5.0
.. _`0.4.2`: https://github.com/spapanik/tvdb_api_client/compare/v0.4.1...v0.4.2
.. _`0.4.1`: https://github.com/spapanik/tvdb_api_client/compare/v0.4.0...v0.4.1
.. _`0.4.0`: https://github.com/spapanik/tvdb_api_client/compare/v0.3.0...v0.4.0
.. _`0.3.0`: https://github.com/spapanik/tvdb_api_client/compare/v0.2.0...v0.3.0
.. _`0.2.0`: https://github.com/spapanik/tvdb_api_client/compare/v0.1.7...v0.2.0
.. _`0.1.7`: https://github.com/spapanik/tvdb_api_client/compare/v0.1.6...v0.1.7
.. _`0.1.6`: https://github.com/spapanik/tvdb_api_client/compare/v0.1.5...v0.1.6
.. _`0.1.5`: https://github.com/spapanik/tvdb_api_client/compare/v0.1.3...v0.1.5
.. _`0.1.3`: https://github.com/spapanik/tvdb_api_client/compare/v0.1.2...v0.1.3
.. _`0.1.2`: https://github.com/spapanik/tvdb_api_client/compare/v0.1.0...v0.1.2
.. _`0.1.0`: https://github.com/spapanik/tvdb_api_client/compare/v0.0.2...v0.1.0
.. _`0.0.2`: https://github.com/spapanik/tvdb_api_client/compare/v0.0.1...v0.0.2
.. _`0.0.1`: https://github.com/spapanik/tvdb_api_client/releases/tag/v0.0.1

.. _`Keep a Changelog`: https://keepachangelog.com/en/1.0.0/
.. _`Semantic Versioning`: https://semver.org/spec/v2.0.0.html
