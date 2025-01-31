from __future__ import annotations

from datetime import date, datetime

from pyutilkit.date_utils import add_timezone

from tvdb_api_client.constants import DATE_FORMAT, DATETIME_FORMAT


def get_tvdb_date(date_string: str) -> date | None:
    if not date_string:
        return None

    naive_datetime = datetime.strptime(date_string, DATE_FORMAT)  # noqa: DTZ007
    return add_timezone(naive_datetime).date()


def get_tvdb_datetime(datetime_string: str) -> datetime | None:
    if not datetime_string:
        return None

    naive_datetime = datetime.strptime(datetime_string, DATETIME_FORMAT)  # noqa: DTZ007
    return add_timezone(naive_datetime)
