from __future__ import annotations

import json
from base64 import urlsafe_b64decode
from datetime import datetime
from typing import Any, cast

import requests
from pathurl import URL

from tvdb_api_client.dataclasses import Episode, Series

BASE_V3_URL = URL("https://api.thetvdb.com/")
BASE_V4_URL = URL("https://api4.thetvdb.com/v4/")


class _Cache(dict):  # type: ignore[type-arg]
    def set(self, key, value):  # noqa: A003
        self[key] = value


class TVDBClientV3:
    __slots__ = ["_auth_data", "_cache", "_urls", "_default_language"]
    _cache_token_key = "tvdb_token"

    def __init__(
        self, username, user_key, api_key, cache=None, language: str | None = None
    ):
        self._auth_data = {"username": username, "userkey": user_key, "apikey": api_key}
        self._cache = cache or _Cache()
        self._urls = self._generate_urls()
        self._load_default_language(language)

    @staticmethod
    def _generate_urls():
        urls = {
            "login": "/login",
            "refresh_token": "/refresh_token",
            "search_series": "/search/series",
            "series": "/series/{id}",
            "series_episodes": "/series/{id}/episodes",
            "user": "/user",
        }

        return {key: BASE_V3_URL.join(url).string for key, url in urls.items()}

    def _load_default_language(self, language: str | None = None):
        if language is None:
            self._default_language = None
            url = self._urls["user"]
            self._default_language = self._get(url)["data"]["language"]
        else:
            self._default_language = language

    def _generate_token(self):
        url = self._urls["login"]
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        response = requests.post(url, headers=headers, data=json.dumps(self._auth_data))
        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid credentials.")

        if response.status_code != 200:
            raise ConnectionError("Unexpected Response.")

        return json.loads(response.content.decode("utf-8"))["token"]

    def _get_with_token(self, url, query_params=None, language: str | None = None):
        token = self._cache.get(self._cache_token_key)
        if token is None:
            token = self._generate_token()
            self._cache.set(self._cache_token_key, token)

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Accept-Language": language or self._default_language,
        }
        return requests.get(url, headers=headers, params=query_params)

    def _update_token(self):
        response = self._get_with_token(self._urls["refresh_token"])
        if response.status_code == 200:
            token = json.loads(response.content.decode("utf-8"))["token"]
            self._cache.set(self._cache_token_key, token)

        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid token")

        raise ConnectionError("Unexpected Response.")

    def _get(
        self, url, query_params=None, *, allow_401=True, language: str | None = None
    ):
        response = self._get_with_token(url, query_params, language)
        if response.status_code == 200:
            return json.loads(response.content.decode("utf-8"))

        elif response.status_code == 404:
            raise LookupError("There are no data for this term.")

        elif response.status_code == 401 and allow_401:
            try:
                self._update_token()
            except ConnectionError:
                token = self._generate_token()
                self._cache.set(self._cache_token_key, token)

            return self._get(url, allow_401=False)

        raise ConnectionError("Unexpected Response.")

    def get_series_by_id(
        self,
        tvdb_id: str | int,
        *,
        refresh_cache: bool = False,
        language: str | None = None,
    ) -> dict[str, Any]:
        """Get the series info by its tvdb ib"""
        key = f"get_series_by_id::tvdb_id:{tvdb_id}"
        data: dict[str, Any] = self._cache.get(key)
        if data is None or refresh_cache:
            url = self._urls["series"].format(id=tvdb_id)
            data = self._get(url, language=language)["data"]
            self._cache.set(key, data)
        return data

    def get_series_by_imdb_id(
        self, imdb_id: str, *, refresh_cache: bool = False, language: str | None = None
    ) -> dict[str, Any]:
        """Get the series info by its imdb id"""
        key = f"get_series_by_imdb_id::imdb_id:{imdb_id}"
        data: dict[str, Any] = self._cache.get(key)
        if data is None or refresh_cache:
            url = self._urls["search_series"]
            query_params = {"imdbId": imdb_id}
            tvdb_id = self._get(url, query_params, language=language)["data"][0]["id"]
            data = self.get_series_by_id(tvdb_id)
            self._cache.set(key, data)
        return data

    def find_series_by_name(
        self,
        series_name: str,
        *,
        refresh_cache: bool = False,
        language: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        Find all TV series that match a TV series name

        The info returned for each TV series are its name,
        the original air date (in "%Y-%m-%d" format) and the
        tvdb_id (as an integer).

        This information should be enough to identify the desired
        series and search by id afterwards.
        """
        key = f"find_series_by_name::series_name:{series_name}"
        data: list[dict[str, Any]] = self._cache.get(key)
        if data is None or refresh_cache:
            url = self._urls["search_series"]
            query_params = {"name": series_name}
            info = self._get(url, query_params, language=language)["data"]
            data = [
                {
                    "name": series["seriesName"],
                    "air_date": series["firstAired"],
                    "tvdb_id": series["id"],
                }
                for series in info
            ]
            self._cache.set(key, data)
        return data

    def get_episodes_by_series(
        self,
        tvdb_id: str | int,
        refresh_cache: bool = False,
        language: str | None = None,
    ) -> list[dict[str, Any]]:
        """Get all the episodes for a TV series"""
        key = f"get_episodes_by_series::tvdb_id:{tvdb_id}"
        data: list[dict[str, Any]] = self._cache.get(key)
        if data is None or refresh_cache:
            base_url = self._urls["series_episodes"].format(id=tvdb_id)
            full_data = self._get(base_url, language=language)
            data = full_data["data"]
            number_of_pages = int(full_data["links"]["last"])
            url = base_url + "?page={page_number}"
            for page_number in range(2, number_of_pages + 1):
                data += self._get(
                    url.format(page_number=page_number), language=language
                )["data"]
            self._cache.set(key, data)
        return data


class TVDBClientV4:
    __slots__ = ["_auth_data", "_cache"]

    def __init__(self, api_key: str, cache=None, pin: str | None = None):
        self._auth_data = {"apikey": api_key}
        if pin is not None:
            self._auth_data["pin"] = pin
        self._cache = cache or _Cache()

    @staticmethod
    def _get_expiry(token: str) -> int:
        if token is None:
            return 0

        header, payload, *_ = token.split(".")
        padding = "=" * (4 - len(payload) % 4)
        data = json.loads(urlsafe_b64decode(payload + padding).decode())
        return cast(int, data["exp"])

    def _generate_token(self):
        login_endpoint = "login"
        url = BASE_V4_URL.join(login_endpoint)
        headers = {"Content-Type": "application/json", "accept": "application/json"}
        response = requests.post(
            url.string, headers=headers, data=json.dumps(self._auth_data)
        )
        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid credentials.")

        if response.status_code != 200:
            raise ConnectionError("Unexpected Response.")

        return response.json()["data"]["token"]

    def _get(self, url: URL):
        cache_token_key = "tvdb_v4_token"
        token = self._cache.get(cache_token_key)
        if self._get_expiry(token) < datetime.utcnow().timestamp() + 60:
            token = self._generate_token()
            self._cache.set(cache_token_key, token)

        headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}
        response = requests.get(url.string, headers=headers)

        if response.status_code == 200:
            return response.json()

        elif response.status_code in {400, 404}:
            raise LookupError("There are no data for this term.")

        elif response.status_code == 401:
            raise ConnectionRefusedError("Invalid credentials.")

        raise ConnectionError("Unexpected Response.")

    def get_raw_series_by_id(
        self, tvdb_id: int, *, refresh_cache: bool = False
    ) -> dict[str, Any]:
        """Get the series info by its tvdb ib as returned by the TVDB"""
        key = f"get_series_by_id::tvdb_id:{tvdb_id}"
        data: dict[str, Any] = self._cache.get(key)
        if data is None or refresh_cache:
            url = BASE_V4_URL.join(f"series/{tvdb_id}")
            data = self._get(url)["data"]
            self._cache.set(key, data)
        return data

    def get_series_by_id(self, tvdb_id: int, *, refresh_cache: bool = False) -> Series:
        raw_data = self.get_raw_series_by_id(tvdb_id, refresh_cache=refresh_cache)
        return Series.from_raw_data(raw_data)

    def get_raw_episodes_by_series(
        self, tvdb_id: int, season_type: str = "default", *, refresh_cache: bool = False
    ) -> list[dict[str, Any]]:
        """Get all the episodes for a TV series as returned by the TVDB"""
        key = f"get_episodes_by_series::tvdb_id:{tvdb_id}"
        data: list[dict[str, Any]] = self._cache.get(key)
        if data is None or refresh_cache:
            base_url = BASE_V4_URL.join(f"series/{tvdb_id}/episodes/{season_type}")
            full_data = self._get(base_url)
            data = full_data["data"]["episodes"]
            self._cache.set(key, data)
        return data

    def get_episodes_by_series(
        self, tvdb_id: int, season_type: str = "default", *, refresh_cache: bool = False
    ) -> list[Episode]:
        """Get all the episodes for a TV series"""
        raw_data = self.get_raw_episodes_by_series(
            tvdb_id, season_type, refresh_cache=refresh_cache
        )
        return [Episode.from_raw_data(episode_info) for episode_info in raw_data]


TVDBClient = TVDBClientV3
