from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from pathurl import URL

from tvdb_api_client.utils import get_tvdb_date, get_tvdb_datetime

if TYPE_CHECKING:
    from datetime import date, datetime

    from tvdb_api_client.lib.type_defs import (
        AliasRawData,
        EpisodeRawData,
        SeriesRawData,
        StatusRawData,
    )


@dataclass
class Alias:
    language: str
    name: str

    @classmethod
    def from_raw_data(cls, raw_data: AliasRawData) -> Alias:
        return cls(language=raw_data["language"], name=raw_data["name"])


@dataclass
class Status:
    id: int
    name: str
    record_type: str
    keep_updated: bool

    @classmethod
    def from_raw_data(cls, raw_data: StatusRawData) -> Status:
        return cls(
            id=raw_data["id"],
            name=raw_data["name"],
            record_type=raw_data["recordType"],
            keep_updated=raw_data["keepUpdated"],
        )


@dataclass
class Series:
    id: int
    name: str
    slug: str
    image: URL | None
    name_translations: list[str]
    overview_translations: list[str]
    aliases: list[Alias]
    first_aired: date | None
    last_aired: date | None
    next_aired: date | None
    score: float
    status: Status
    original_country: str
    original_language: str
    default_season_type: int
    is_order_randomized: bool
    last_updated: datetime | None
    average_runtime: int
    overview: str

    @classmethod
    def from_raw_data(cls, raw_data: SeriesRawData) -> Series:
        image_url = raw_data["image"]
        return cls(
            id=raw_data["id"],
            name=raw_data["name"],
            slug=raw_data["slug"],
            image=URL(image_url) if image_url else None,
            name_translations=raw_data["nameTranslations"],
            overview_translations=raw_data["overviewTranslations"],
            aliases=[Alias.from_raw_data(alias) for alias in raw_data["aliases"]],
            first_aired=get_tvdb_date(raw_data["firstAired"]),
            last_aired=get_tvdb_date(raw_data["lastAired"]),
            next_aired=get_tvdb_date(raw_data["nextAired"]),
            score=raw_data["score"],
            status=Status.from_raw_data(raw_data["status"]),
            original_country=raw_data["originalCountry"],
            original_language=raw_data["originalLanguage"],
            default_season_type=raw_data["defaultSeasonType"],
            is_order_randomized=raw_data["isOrderRandomized"],
            last_updated=get_tvdb_datetime(raw_data["lastUpdated"]),
            average_runtime=raw_data["averageRuntime"],
            overview=raw_data["overview"],
        )


@dataclass
class Episode:
    id: int
    series_id: int
    name: str
    aired: date | None
    runtime: int
    name_translations: list[str]
    overview: str
    overview_translations: list[str]
    image: URL | None
    image_type: int
    is_movie: int
    number: int
    season_number: int
    last_updated: datetime | None
    finale_type: str

    @classmethod
    def from_raw_data(cls, raw_data: EpisodeRawData) -> Episode:
        image_url = raw_data["image"]
        return cls(
            id=raw_data["id"],
            series_id=raw_data["seriesId"],
            name=raw_data["name"],
            aired=get_tvdb_date(raw_data["aired"]),
            runtime=raw_data["runtime"],
            name_translations=raw_data["nameTranslations"],
            overview=raw_data["overview"],
            overview_translations=raw_data["overviewTranslations"],
            image=URL(image_url) if image_url else None,
            image_type=raw_data["imageType"],
            is_movie=raw_data["isMovie"],
            number=raw_data["number"],
            season_number=raw_data["seasonNumber"],
            last_updated=get_tvdb_datetime(raw_data["lastUpdated"]),
            finale_type=raw_data["finaleType"],
        )
