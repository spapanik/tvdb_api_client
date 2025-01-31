from __future__ import annotations

from typing import Any, Protocol, TypedDict  # upgrade: py3.9: remove Union


class AbstractCache(Protocol):
    def set(self, key: str, value: object) -> None: ...
    def get(self, key: str) -> Any: ...  # type: ignore[misc]  # noqa: ANN401


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
    episodes: EpisodeRawData | None
    year: str


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
    seasons: int | None
    absoluteNumber: int
    year: str


class FullRawData(TypedDict):
    series: SeriesRawData
    episodes: list[EpisodeRawData]
