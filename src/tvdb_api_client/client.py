from __future__ import annotations

import json
from base64 import urlsafe_b64decode
from typing import Any, cast

import requests
from pathurl import URL

from tvdb_api_client.dataclasses import Episode, Series
from tvdb_api_client.utils import now

BASE_API_URL = URL("https://api4.thetvdb.com/v4/")


class _Cache(dict):  # type: ignore[type-arg]
    def set(self, key, value):  # noqa: A003
        self[key] = value


class TVDBClient:
    __slots__ = ["_auth_data", "_cache"]

    def __init__(self, api_key: str, cache=None, pin: str | None = None):
        self._auth_data = {"apikey": api_key}
        if pin is not None:
            self._auth_data["pin"] = pin
        self._cache = cache or _Cache()

    @staticmethod
    def _get_expiry(token: str | None) -> int:
        if token is None:
            return 0

        header, payload, *_ = token.split(".")
        padding = "=" * (4 - len(payload) % 4)
        data = json.loads(urlsafe_b64decode(payload + padding).decode())
        return cast(int, data["exp"])

    def _generate_token(self):
        login_endpoint = "login"
        url = BASE_API_URL.join(login_endpoint)
        headers = {"Content-Type": "application/json", "accept": "application/json"}
        response = requests.post(
            url.string,
            headers=headers,
            data=json.dumps(self._auth_data),
            timeout=(60, 120),
        )
        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid credentials.")

        if response.status_code != 200:
            raise ConnectionError("Unexpected Response.")

        return response.json()["data"]["token"]

    def _get(self, url: URL):
        cache_token_key = "tvdb_v4_token"  # noqa: S105
        token = self._cache.get(cache_token_key)
        if self._get_expiry(token) < now().timestamp() + 60:
            token = self._generate_token()
            self._cache.set(cache_token_key, token)

        headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}
        response = requests.get(url.string, headers=headers, timeout=(60, 120))

        if response.status_code == 200:
            return response.json()

        if response.status_code in {400, 404}:
            raise LookupError("There are no data for this term.")

        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid credentials.")

        raise ConnectionError("Unexpected Response.")

    def get_raw_series_by_id(
        self, tvdb_id: int, *, refresh_cache: bool = False
    ) -> dict[str, Any]:
        """Get the series info by its tvdb ib as returned by the TVDB"""
        key = f"get_series_by_id::tvdb_id:{tvdb_id}"
        data: dict[str, Any] | None = self._cache.get(key)
        if data is None or refresh_cache:
            url = BASE_API_URL.join(f"series/{tvdb_id}")
            data = self._get(url)["data"] or {}
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
        data: list[dict[str, Any]] | None = self._cache.get(key)
        if data is None or refresh_cache:
            base_url = BASE_API_URL.join(f"series/{tvdb_id}/episodes/{season_type}")
            full_data = self._get(base_url)
            data = full_data["data"]["episodes"] or []
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
