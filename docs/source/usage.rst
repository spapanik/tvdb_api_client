=====
Usage
=====

.. py:module:: tvdb_api_client

The central object is the ``TVDBClient`` client which needs the ``username``, ``user_key``, and ``api_key`` supplied by the TVDB.
It can be initialised with a cache (optionally), and if no cache is passed a dummy cache object will be created.

.. note::

    It is advisable to use a cache that will persist during a server restart, so that the token will not have to be regenerated.

.. warning::

    Please be advised that the token will be stored in the default cache in plaintext, so if there are any security considerations they should be taken care into account when choosing the cache.


.. py:class:: TVDBClient

    The TVDB client

    .. py:method:: __init__( \
            username, \
            user_key, \
            api_key, \
            cache=None, \
            language=None \
        )

       :param str username: The TVDB username
       :param str user_key: The TVDB user key
       :param str api_key: The TVDB api key
       :param cache: The caching object to be used
       :param str language: The 2-letter language code

       Initialise the TVDB client

    .. py:method:: get_series_by_id( \
            tvdb_id, \
            *, \
            refresh_cache=False, \
            language=None, \
        )

       :param str | int tvdb_id: The TVDB id of the series
       :param bool refresh_cache: Whether to use or not cached responses
       :param str language: The 2-letter code, if overriding the client's language is needed
       :return: A dictionary of the series info
       :rtype: dict

       Get the series info by its tvdb id

    .. py:method:: get_series_by_imdb_id( \
            imdb_id, \
            *, \
            refresh_cache=False, \
            language=None, \
        )

       :param str imdb_id: The imdb id of the series
       :param bool refresh_cache: Whether to use or not cached responses
       :param str language: The 2-letter code, if overriding the client's language is needed
       :return: A dictionary of the series info
       :rtype: dict

        Get the series info by its imdb id

    .. py:method:: find_series_by_name( \
            series_name, \
            *, \
            refresh_cache=False, \
            language=None, \
        )

       :param str series_name: The series' name
       :param bool refresh_cache: Whether to use or not cached responses
       :param str language: The 2-letter code, if overriding the client's language is needed
       :return: A list of all the series that match the name
       :rtype: list[dict]

       Find all TV series that match a TV series name

       The info returned for each TV series are its name,
       the original air date (in "%Y-%m-%d" format) and the
       tvdb_id (as an integer).

       This information should be enough to identify the desired
       series and search by id afterwards.

    .. py:method:: get_episodes_by_series( \
            tvdb_id: str | int, \
            *, \
            refresh_cache=False, \
            language=None, \
        )

       :param str | int tvdb_id: The TVDB id of the series
       :param bool refresh_cache: Whether to use or not cached responses
       :param str language: The 2-letter code, if overriding the client's language is needed
       :return: A list of all the episodes
       :rtype: list[dict]

        Get all the episodes for a TV series

.. note::
    Also, all of these methods will used the cached value if present. To get new data, you may pass ``refresh_cache=True`` to all of them.
