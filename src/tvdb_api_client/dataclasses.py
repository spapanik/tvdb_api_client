from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any

from pathurl import URL

from tvdb_api_client.utils import get_tvdb_date, get_tvdb_datetime


@dataclass
class Alias:
    language: str
    name: str

    @classmethod
    def from_raw_data(cls, raw_data: dict[str, Any]) -> Alias:
        return cls(language=raw_data.get("language"), name=raw_data.get("name"))


@dataclass
class Status:
    id: int  # noqa: A003
    name: str
    record_type: str
    keep_updated: bool

    @classmethod
    def from_raw_data(cls, raw_data: dict[str, Any]) -> Status:
        return cls(
            id=raw_data.get("id"),
            name=raw_data.get("name"),
            record_type=raw_data.get("recordType"),
            keep_updated=raw_data.get("keepUpdated"),
        )


@dataclass
class Series:
    id: int  # noqa: A003
    name: str
    slug: str
    image: URL
    name_translations: list[str]
    overview_translations: list[str]
    aliases: list[Alias]
    first_aired: date
    last_aired: date
    next_aired: date
    score: float
    status: Status
    original_country: str
    original_language: str
    default_season_type: int
    is_order_randomized: bool
    last_updated: datetime
    average_runtime: int
    overview: str

    @classmethod
    def from_raw_data(cls, raw_data: dict[str, Any]) -> Series:
        return cls(
            id=raw_data.get("id"),
            name=raw_data.get("name"),
            slug=raw_data.get("slug"),
            image=URL(raw_data.get("image")),
            name_translations=raw_data.get("nameTranslations"),
            overview_translations=raw_data.get("overviewTranslations"),
            aliases=[Alias.from_raw_data(alias) for alias in raw_data.get("aliases")],
            first_aired=get_tvdb_date(raw_data.get("firstAired")),
            last_aired=get_tvdb_date(raw_data.get("lastAired")),
            next_aired=get_tvdb_date(raw_data.get("nextAired")),
            score=raw_data.get("score"),
            status=Status.from_raw_data(raw_data.get("status")),
            original_country=raw_data.get("originalCountry"),
            original_language=raw_data.get("originalLanguage"),
            default_season_type=raw_data.get("defaultSeasonType"),
            is_order_randomized=raw_data.get("isOrderRandomized"),
            last_updated=get_tvdb_datetime(raw_data.get("lastUpdated")),
            average_runtime=raw_data.get("averageRuntime"),
            overview=raw_data.get("overview"),
        )


@dataclass
class Episode:
    id: int  # noqa: A003
    series_id: int
    name: str
    aired: date
    runtime: int
    name_translations: list[str]
    overview: str
    overview_translations: list[str]
    image: URL
    image_type: int
    is_movie: int
    number: int
    season_number: int
    last_updated: datetime
    finale_type: str

    @classmethod
    def from_raw_data(cls, raw_data: dict[str, Any]) -> Episode:
        return cls(
            id=raw_data.get("id"),
            series_id=raw_data.get("seriesId"),
            name=raw_data.get("name"),
            aired=get_tvdb_date(raw_data.get("aired")),
            runtime=raw_data.get("runtime"),
            name_translations=raw_data.get("nameTranslations"),
            overview=raw_data.get("overview"),
            overview_translations=raw_data.get("overviewTranslations"),
            image=URL(raw_data.get("image")),
            image_type=raw_data.get("imageType"),
            is_movie=raw_data.get("isMovie"),
            number=raw_data.get("number"),
            season_number=raw_data.get("seasonNumber"),
            last_updated=get_tvdb_datetime(raw_data.get("lastUpdated")),
            finale_type=raw_data.get("finaleType"),
        )
