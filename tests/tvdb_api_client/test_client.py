from tvdb_api_client import client


class TestCache:
    @staticmethod
    def test_set():
        cache = client._Cache()
        cache.set("attribute", "value")
        assert cache.get("attribute") == "value"


class TestTVDBClient:
    @staticmethod
    def test_init_without_cache():
        client.TVDBClient("username", "key", "api_key", language="eng")

    @staticmethod
    def test_init_default_language():
        api = client.TVDBClient("username", "key", "api_key", language="eng")
        assert api._default_language == "eng"
