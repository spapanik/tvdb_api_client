from __future__ import annotations

from datetime import date, datetime, timezone

from tvdb_api_client.constants import DATE_FORMAT, DATETIME_FORMAT


def get_tvdb_date(date_string: str) -> date | None:
    if not date_string:
        return None

    return (
        datetime.strptime(date_string, DATE_FORMAT).replace(tzinfo=timezone.utc).date()
    )


def get_tvdb_datetime(datetime_string: str) -> datetime | None:
    if not datetime_string:
        return None

    return datetime.strptime(datetime_string, DATETIME_FORMAT).replace(
        tzinfo=timezone.utc
    )


def now() -> datetime:
    return datetime.now(timezone.utc)
