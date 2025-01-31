from __future__ import annotations

from typing import TYPE_CHECKING

from tvdb_api_client import models

if TYPE_CHECKING:
    from tvdb_api_client.lib.type_defs import (
        AliasRawData,
        EpisodeRawData,
        SeriesRawData,
        StatusRawData,
    )


def test_alias(raw_alias_data: AliasRawData) -> None:
    alias = models.Alias.from_raw_data(raw_alias_data)
    assert alias.language == raw_alias_data["language"]


def test_episode(raw_episode_data: EpisodeRawData) -> None:
    episode = models.Episode.from_raw_data(raw_episode_data)
    assert episode.id == raw_episode_data["id"]


def test_status(raw_status_data: StatusRawData) -> None:
    status = models.Status.from_raw_data(raw_status_data)
    assert status.id == raw_status_data["id"]


def test_series(raw_series_data: SeriesRawData) -> None:
    series = models.Series.from_raw_data(raw_series_data)
    assert series.id == raw_series_data["id"]
