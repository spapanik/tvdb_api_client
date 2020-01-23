from tvdb_api_client import client


class TestTVDBClient:
    @staticmethod
    def test_init():
        client.TVDBClient("username", "key", "api_key", {})
