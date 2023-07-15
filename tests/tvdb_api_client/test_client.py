from tvdb_api_client import client


class TestCache:
    @staticmethod
    def test_set() -> None:
        cache = client._Cache()  # noqa: SLF001
        cache.set("attribute", "value")
        assert cache.get("attribute") == "value"


class TestTVDBClient:
    @staticmethod
    def test_init_without_cache() -> None:
        client.TVDBClient("api_key")
