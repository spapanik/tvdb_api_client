from __future__ import annotations

from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest

from tvdb_api_client import utils

UTC = ZoneInfo("UTC")


@pytest.mark.parametrize(
    ("date_string", "expected"),
    [("2021-01-02", date(2021, 1, 2)), ("2020-02-29", date(2020, 2, 29)), ("", None)],
)
def test_get_tvdb_date(date_string: str, expected: date) -> None:
    assert utils.get_tvdb_date(date_string) == expected


@pytest.mark.parametrize(
    ("datetime_string", "expected"),
    [
        ("2021-01-02 12:34:56", datetime(2021, 1, 2, 12, 34, 56, tzinfo=UTC)),
        ("", None),
    ],
)
def test_get_tvdb_datetime(datetime_string: str, expected: datetime) -> None:
    assert utils.get_tvdb_datetime(datetime_string) == expected
