import requests
import json


class TVDBClient:
    cache_key = 'tvdb_token'

    tvdb_base_url = 'https://api.thetvdb.com'
    imdb_base_url = 'http://www.imdb.com'

    imdb_series_url = imdb_base_url + '/title/{imdb_id}/'

    episodes_url = tvdb_base_url + '/series/{tvdb_id}/episodes'
    login_url = tvdb_base_url + '/login'
    search_url = tvdb_base_url + '/search/series?imdbId={imdb_id}'
    series_tvdb_url = tvdb_base_url + '/series/{tvdb_id}'
    tvdb_series_info_url = tvdb_base_url + '/search/series?name={series_name}'
    update_token_url = tvdb_base_url + '/refresh_token'

    def __init__(self, apikey, username, userkey, cache):
        self.apikey = apikey
        self.username = username
        self.userkey = userkey
        self.cache = cache
        self._token = self.cache.get(self.cache_key)

    @property
    def token(self):
        if self._token is not None:
            return self._token

        return self._generate_token()

    def _generate_token(self):
        url = self.login_url
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        data = {
            'apikey': self.apikey,
            'username': self.username,
            'userkey': self.userkey,
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code != 200:
            raise ConnectionError('TVDB failed to respond.')

        token = json.loads(response.content.decode('utf-8'))['token']
        self.cache.set(self.cache_key, token)
        self._token = token
        return token

    def _update_token(self):
        token = self._get_data(self.update_token_url).get('token')
        self.cache.set(self.cache_key, token)
        self._token = token

    def _get_data(self, url, *, _allow_update=True):
        token = self.token
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {token}'.format(token=token),
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        elif response.status_code == 401:
            if not _allow_update:
                raise ConnectionError('Unauthorized access')

            self._update_token()
            self._get_data(url, _allow_update=False)

        raise LookupError("Couldn't retrieve any data for this term.")

    def get_tvdb_id(self, imdb_id):
        url = self.search_url.format(imdb_id=imdb_id)
        return self._get_data(url)['data'][0]['id']

    def get_imdb_id(self, tvdb_id):
        url = self.series_tvdb_url.format(tvdb_id=tvdb_id)
        info = self._get_data(url)['data']
        return info['imdbId']

    def find_series_by_name(self, series_name):
        url = self.tvdb_series_info_url.format(series_name=series_name)
        info = self._get_data(url)['data']
        information = [{
            'name': series['seriesName'],
            'air_date': series['firstAired'],
            'tvdb_id': series['id'],
        } for series in info]
        return information

    def get_episodes(self, tvdb_id):
        base_url = self.episodes_url.format(tvdb_id=tvdb_id)
        full_data = self._get_data(base_url)
        data = full_data['data']
        number_of_pages = int(full_data['links']['last'])
        url = base_url + '?page={page_number}'
        for page_number in range(2, number_of_pages + 1):
            data += self._get_data(url.format(page_number=page_number))['data']

        return data
