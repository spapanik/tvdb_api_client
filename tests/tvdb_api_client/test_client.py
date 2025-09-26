from __future__ import annotations

import json
import os
from base64 import urlsafe_b64encode
from http import HTTPStatus
from typing import TYPE_CHECKING
from unittest import mock

import pytest
from pyutilkit.date_utils import now

from tvdb_api_client.client import TheTVDBClient, _Cache

if TYPE_CHECKING:
    from tvdb_api_client.lib.type_defs import EpisodeRawData, SeriesRawData


def test_cache_set() -> None:
    cache = _Cache()
    cache.set("attribute", "value")
    assert cache.get("attribute") == "value"


@mock.patch(
    "tvdb_api_client.client.get_setting",
    new=mock.MagicMock(return_value=None),
)
def test_client_init() -> None:
    with pytest.raises(ValueError, match=r"API Key is required\."):
        TheTVDBClient()
    with pytest.raises(ValueError, match=r"API Key is required\."):
        TheTVDBClient(pin="1234")
    TheTVDBClient(api_key="1234")
    TheTVDBClient(api_key="1234", pin="1234")


def test_client_init_from_env_vars() -> None:
    os.environ["TVDB_API_KEY_V4"] = "1234"
    os.environ["TVDB_PIN_V4"] = "1234"
    TheTVDBClient()


def test_get_raw_series_by_id(
    the_tvdb_client: TheTVDBClient, raw_series_data: SeriesRawData
) -> None:
    with mock.patch.object(
        TheTVDBClient, "get", return_value={"data": raw_series_data}
    ):
        raw_data = the_tvdb_client.get_raw_series_by_id(79509)
    raw_data_from_cache = the_tvdb_client.get_raw_series_by_id(79509)
    assert raw_data == raw_series_data
    assert raw_data == raw_data_from_cache


def test_get_series_by_id(
    the_tvdb_client: TheTVDBClient, raw_series_data: SeriesRawData
) -> None:
    with mock.patch.object(
        TheTVDBClient, "get", return_value={"data": raw_series_data}
    ):
        series = the_tvdb_client.get_series_by_id(79509)
    assert series.id == 79509


def test_get_raw_episodes_by_series(
    the_tvdb_client: TheTVDBClient, raw_episode_data: EpisodeRawData
) -> None:
    with mock.patch.object(
        TheTVDBClient, "get", return_value={"data": {"episodes": [raw_episode_data]}}
    ):
        raw_data = the_tvdb_client.get_raw_episodes_by_series(79509)
    raw_data_from_cache = the_tvdb_client.get_raw_episodes_by_series(79509)
    assert raw_data[0] == raw_episode_data
    assert raw_data == raw_data_from_cache


def test_get_episodes_by_series(
    the_tvdb_client: TheTVDBClient, raw_episode_data: EpisodeRawData
) -> None:
    with mock.patch.object(
        TheTVDBClient, "get", return_value={"data": {"episodes": [raw_episode_data]}}
    ):
        episodes = the_tvdb_client.get_episodes_by_series(79509)
    assert episodes[0].id == 314779


@mock.patch(
    "requests.post",
    new=mock.MagicMock(
        return_value=mock.MagicMock(status_code=HTTPStatus.UNAUTHORIZED)
    ),
)
def test_get_unauthorized() -> None:
    with pytest.raises(ConnectionRefusedError):
        TheTVDBClient(api_key="1234").get("series/79509")


@mock.patch(
    "requests.post",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.IM_A_TEAPOT)),
)
def test_get_unknown_response() -> None:
    with pytest.raises(ConnectionError):
        TheTVDBClient(api_key="1234").get("series/79509")


@mock.patch(
    "requests.get",
    new=mock.MagicMock(
        return_value=mock.MagicMock(status_code=HTTPStatus.UNAUTHORIZED)
    ),
)
@mock.patch(
    "requests.post",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
def test_get_invalid_token() -> None:
    with pytest.raises(ConnectionRefusedError):
        TheTVDBClient(api_key="1234").get("series/79509")


@mock.patch(
    "requests.get",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.NOT_FOUND)),
)
@mock.patch(
    "requests.post",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
def test_get_not_found() -> None:
    with pytest.raises(LookupError):
        TheTVDBClient(api_key="1234").get("series/not_found")


@mock.patch(
    "requests.get",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.IM_A_TEAPOT)),
)
@mock.patch(
    "requests.post",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
def test_get_unknown_get_response() -> None:
    with pytest.raises(ConnectionError):
        TheTVDBClient(api_key="1234").get("series/79509")


@mock.patch(
    "requests.get",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
@mock.patch(
    "requests.post",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
def test_get() -> None:
    TheTVDBClient(api_key="1234").get("series/79509")


@mock.patch(
    "requests.get",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
@mock.patch(
    "requests.post",
    new=mock.MagicMock(return_value=mock.MagicMock(status_code=HTTPStatus.OK)),
)
def test_get_with_cache() -> None:
    client = TheTVDBClient(api_key="1234")
    timestamp = now().timestamp() + 600
    payload = urlsafe_b64encode(json.dumps({"exp": timestamp}).encode()).decode()
    token = f"1234.{payload}.1234"
    client._cache.set("tvdb_v4_token", token)  # noqa: SLF001
    client.get("series/79509")
