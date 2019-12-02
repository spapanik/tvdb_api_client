import json
from typing import List, Union
from urllib.parse import urljoin

import requests


class TVDBClient:
    __slots__ = ["_auth_data", "_cache", "_cache_key", "_saved_token", "_urls"]

    def __init__(self, username, user_key, api_key, cache):
        self._auth_data = {
            "username": username,
            "userkey": user_key,
            "apikey": api_key,
        }
        self._cache = cache
        self._cache_key = "tvdb_token"
        self._saved_token = self._cache.get(self._cache_key)
        self._urls = self._generate_urls()

    @property
    def _token(self):
        if self._saved_token is None:
            self._save_token(self._generate_token())

        return self._saved_token

    @staticmethod
    def _generate_urls():
        tvdb_base_url = "https://api.thetvdb.com"
        urls = {
            "login": "/login",
            "refresh_token": "/refresh_token",
            "search_series": "/search/series",
            "series": "/series/{id}",
            "series_episodes": "/series/{id}/episodes",
        }

        return {key: urljoin(tvdb_base_url, url) for key, url in urls.items()}

    def _save_token(self, token):
        self._saved_token = token
        self._cache.set(self._cache_key, token)

    def _generate_token(self):
        url = self._urls["login"]
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        response = requests.post(url, headers=headers, data=json.dumps(self._auth_data))
        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid credentials.")

        if response.status_code != 200:
            raise ConnectionError("Unexpected Response.")

        return json.loads(response.content.decode("utf-8"))["token"]

    def _get_with_token(self, url, query_params=None):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._token}",
        }
        return requests.get(url, headers=headers, params=query_params)

    def _update_token(self):
        response = self._get_with_token(self._urls["refresh_token"])
        if response.status_code == 200:
            self._save_token(json.loads(response.content.decode("utf-8"))["token"])

        if response.status_code == 401:
            raise ConnectionRefusedError("Invalid token")

        raise ConnectionError("Unexpected Response.")

    def _get(self, url, query_params=None, *, allow_401=True):
        response = self._get_with_token(url, query_params)
        if response.status_code == 200:
            return json.loads(response.content.decode("utf-8"))

        elif response.status_code == 404:
            raise LookupError("There are no data for this term.")

        elif response.status_code == 401 and allow_401:
            try:
                self._update_token()
            except ConnectionError:
                self._save_token(self._generate_token())

            return self._get(url, allow_401=False)

        raise ConnectionError("Unexpected Response.")

    def get_series_by_id(self, tvdb_id: Union[str, int]) -> dict:
        """
        Get the series info by its tvdb ib
        """
        url = self._urls["series"].format(id=tvdb_id)
        return self._get(url)["data"]

    def get_series_by_imdb_id(self, imdb_id: str) -> dict:
        """
        Get the series info by its imdb ib
        """
        url = self._urls["search_series"]
        query_params = {"imdbId": imdb_id}
        tvdb_id = self._get(url, query_params)["data"][0]["id"]
        return self.get_series_by_id(tvdb_id)

    def find_series_by_name(self, series_name: str) -> List[dict]:
        """
        Find all TV series that match a TV series name

        The info returned for each TV series are its name,
        the original air date (in "%Y-%m-%d" format) and the
        tvdb_id (as an integer).

        This information should be enough to identify the desired
        series and search by id afterwards.
        """
        url = self._urls["search_series"]
        query_params = {"name": series_name}
        info = self._get(url, query_params)["data"]

        return [
            {
                "name": series["seriesName"],
                "air_date": series["firstAired"],
                "tvdb_id": series["id"],
            }
            for series in info
        ]

    def get_episodes_by_series(self, tvdb_id: Union[str, int]) -> List[dict]:
        """
        Get all the episodes for a TV series
        """
        base_url = self._urls["series_episodes"].format(id=tvdb_id)
        full_data = self._get(base_url)
        data = full_data["data"]
        number_of_pages = int(full_data["links"]["last"])
        url = base_url + "?page={page_number}"
        for page_number in range(2, number_of_pages + 1):
            data += self._get(url.format(page_number=page_number))["data"]

        return data
