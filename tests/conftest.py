from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tvdb_api_client.client import TheTVDBClient

if TYPE_CHECKING:
    from tvdb_api_client.lib.type_defs import (
        AliasRawData,
        EpisodeRawData,
        SeriesRawData,
        StatusRawData,
    )


@pytest.fixture
def raw_alias_data() -> AliasRawData:
    return {"language": "fas", "name": "فرندز"}


@pytest.fixture
def raw_status_data() -> StatusRawData:
    return {"id": 2, "name": "Ended", "recordType": "series", "keepUpdated": False}


@pytest.fixture
def raw_series_data() -> SeriesRawData:
    return {
        "id": 79509,
        "name": "Day Break",
        "slug": "day-break",
        "image": "https://artworks.thetvdb.com/banners/posters/79509-1.jpg",
        "nameTranslations": [
            "ces",
            "deu",
            "eng",
            "fra",
            "heb",
            "ita",
            "pol",
            "por",
            "rus",
            "spa",
        ],
        "overviewTranslations": [
            "ces",
            "deu",
            "eng",
            "fra",
            "heb",
            "ita",
            "pol",
            "por",
            "rus",
            "spa",
        ],
        "aliases": [],
        "firstAired": "2006-11-15",
        "lastAired": "2008-03-22",
        "nextAired": "",
        "score": 15382,
        "status": {
            "id": 2,
            "name": "Ended",
            "recordType": "series",
            "keepUpdated": False,
        },
        "originalCountry": "usa",
        "originalLanguage": "eng",
        "defaultSeasonType": 1,
        "isOrderRandomized": False,
        "lastUpdated": "2024-03-06 07:47:24",
        "averageRuntime": 45,
        "episodes": None,
        "overview": (
            "Today Detective Brett Hopper will be accused of shooting state attorney "
            "Alberto Garza. He will offer his rock solid alibi. He will realize he's "
            "been framed. And he will run. Then, he will wake up and start the day "
            "over again."
        ),
        "year": "2006",
    }


@pytest.fixture
def raw_episode_data() -> EpisodeRawData:
    return {
        "id": 314779,
        "seriesId": 79509,
        "name": "What if It's Him?",
        "aired": "2008-03-22",
        "runtime": 45,
        "nameTranslations": ["eng", "fra", "heb", "ita", "rus", "spa"],
        "overview": (
            'Hopper finally breaks the day and sees "tomorrow," '
            "only to find out that the next day brings more problems with it."
        ),
        "overviewTranslations": ["ces", "eng", "fra", "heb", "ita", "rus"],
        "image": "https://artworks.thetvdb.com/banners/episodes/79509/314779.jpg",
        "imageType": 11,
        "isMovie": 0,
        "seasons": None,
        "number": 13,
        "absoluteNumber": 0,
        "seasonNumber": 1,
        "lastUpdated": "2024-03-06 07:44:49",
        "finaleType": "series",
        "year": "2008",
    }


@pytest.fixture
def the_tvdb_client() -> TheTVDBClient:
    return TheTVDBClient(api_key="1234", pin="1234")
