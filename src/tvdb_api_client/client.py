from __future__ import annotations

import json
from base64 import urlsafe_b64decode
from http import HTTPStatus
from typing import Any, Protocol, Union, cast  # upgrade: py3.9: remove Union

import requests
from pathurl import URL

from tvdb_api_client.dataclasses import Episode, Series
from tvdb_api_client.lib.types import EpisodeRawData, FullRawData, SeriesRawData
from tvdb_api_client.utils import now

BASE_API_URL = URL("https://api4.thetvdb.com/v4/")


class AbstractCache(Protocol):
    def set(self, key: str, value: object) -> None: ...
    def get(self, key: str) -> Any: ...  # type: ignore[misc]  # noqa: ANN401


class _Cache(dict):  # type: ignore[type-arg]
    def set(self, key: str, value: object) -> None:
        self[key] = value


class TVDBClient:
    __slots__ = ["_auth_data", "_cache"]

    def __init__(
        self, api_key: str, cache: AbstractCache | None = None, pin: str | None = None
    ) -> None:
        self._auth_data = {"apikey": api_key}
        if pin is not None:
            self._auth_data["pin"] = pin
        self._cache = cache or _Cache()

    @staticmethod
    def _get_expiry(token: str | None) -> int:
        if token is None:
            return 0

        _, payload, *_ = token.split(".")
        padding = "=" * (4 - len(payload) % 4)
        data = json.loads(urlsafe_b64decode(payload + padding).decode())
        return cast(int, data["exp"])

    def _generate_token(self) -> str:
        login_endpoint = "login"
        url = BASE_API_URL.join(login_endpoint)
        headers = {"Content-Type": "application/json", "accept": "application/json"}
        response = requests.post(
            url.string,
            headers=headers,
            data=json.dumps(self._auth_data),
            timeout=(60, 120),
        )
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            msg = "Invalid credentials."
            raise ConnectionRefusedError(msg)

        if response.status_code != HTTPStatus.OK:
            msg = "Unexpected Response."
            raise ConnectionError(msg)

        return cast(str, response.json()["data"]["token"])

    def _get(self, url: URL) -> dict[str, object]:
        cache_token_key = "tvdb_v4_token"  # noqa: S105
        token = cast(Union[str, None], self._cache.get(cache_token_key))
        if self._get_expiry(token) < now().timestamp() + 60:
            token = self._generate_token()
            self._cache.set(cache_token_key, token)

        headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}
        response = requests.get(url.string, headers=headers, timeout=(60, 120))

        if response.status_code == HTTPStatus.OK:
            return cast(dict[str, object], response.json())

        if response.status_code in {HTTPStatus.BAD_REQUEST, HTTPStatus.NOT_FOUND}:
            msg = "There are no data for this term."
            raise LookupError(msg)

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            msg = "Invalid credentials."
            raise ConnectionRefusedError(msg)

        msg = "Unexpected Response."
        raise ConnectionError(msg)

    def get_raw_series_by_id(
        self, tvdb_id: int, *, refresh_cache: bool = False
    ) -> SeriesRawData:
        """Get the series info by its tvdb ib as returned by the TVDB."""
        key = f"get_series_by_id::tvdb_id:{tvdb_id}"
        data = cast(Union[SeriesRawData, None], self._cache.get(key))
        if data is None or refresh_cache:
            url = BASE_API_URL.join(f"series/{tvdb_id}")
            data = cast(SeriesRawData, self._get(url)["data"])
            self._cache.set(key, data)
        return data

    def get_series_by_id(self, tvdb_id: int, *, refresh_cache: bool = False) -> Series:
        raw_data = self.get_raw_series_by_id(tvdb_id, refresh_cache=refresh_cache)
        return Series.from_raw_data(raw_data)

    def get_raw_episodes_by_series(
        self, tvdb_id: int, season_type: str = "default", *, refresh_cache: bool = False
    ) -> list[EpisodeRawData]:
        """Get all the episodes for a TV series as returned by the TVDB."""
        key = f"get_episodes_by_series::tvdb_id:{tvdb_id}"
        data = cast(Union[list[EpisodeRawData], None], self._cache.get(key))
        if data is None or refresh_cache:
            base_url = BASE_API_URL.join(f"series/{tvdb_id}/episodes/{season_type}")
            full_data = cast(FullRawData, self._get(base_url)["data"])
            data = full_data["episodes"]
            self._cache.set(key, data)
        return data

    def get_episodes_by_series(
        self, tvdb_id: int, season_type: str = "default", *, refresh_cache: bool = False
    ) -> list[Episode]:
        """Get all the episodes for a TV series."""
        raw_data = self.get_raw_episodes_by_series(
            tvdb_id, season_type, refresh_cache=refresh_cache
        )
        return [Episode.from_raw_data(episode_info) for episode_info in raw_data]
