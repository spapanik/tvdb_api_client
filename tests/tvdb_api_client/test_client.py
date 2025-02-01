import os
from unittest import mock

import pytest

from tvdb_api_client import client


class TestCache:
    @staticmethod
    def test_set() -> None:
        cache = client._Cache()  # noqa: SLF001
        cache.set("attribute", "value")
        assert cache.get("attribute") == "value"


class TestTVDBClient:
    @staticmethod
    @mock.patch(
        "tvdb_api_client.client.get_setting",
        new=mock.MagicMock(return_value=None),
    )
    def test_init() -> None:
        with pytest.raises(ValueError, match="API Key is required."):
            client.TheTVDBClient()
        with pytest.raises(ValueError, match="API Key is required."):
            client.TheTVDBClient(pin="1234")
        client.TheTVDBClient(api_key="1234")
        client.TheTVDBClient(api_key="1234", pin="1234")

    @staticmethod
    def test_init_from_env_vars() -> None:
        os.environ["TVDB_API_KEY_V4"] = "1234"
        os.environ["TVDB_PIN_V4"] = "1234"
        client.TheTVDBClient()
