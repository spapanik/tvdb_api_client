from __future__ import annotations

from typing import TypedDict


class AliasRawData(TypedDict):
    language: str
    name: str


class StatusRawData(TypedDict):
    id: int
    name: str
    recordType: str
    keepUpdated: bool


class SeriesRawData(TypedDict):
    id: int
    name: str
    slug: str
    image: str | None
    nameTranslations: list[str]
    overviewTranslations: list[str]
    aliases: list[AliasRawData]
    firstAired: str
    lastAired: str
    nextAired: str
    score: float
    status: StatusRawData
    originalCountry: str
    originalLanguage: str
    defaultSeasonType: int
    isOrderRandomized: bool
    lastUpdated: str
    averageRuntime: int
    overview: str


class EpisodeRawData(TypedDict):
    id: int
    seriesId: int
    name: str
    aired: str
    runtime: int
    nameTranslations: list[str]
    overview: str
    overviewTranslations: list[str]
    image: str
    imageType: int
    isMovie: int
    number: int
    seasonNumber: int
    lastUpdated: str
    finaleType: str


class FullRawData(TypedDict):
    series: SeriesRawData
    episodes: list[EpisodeRawData]
