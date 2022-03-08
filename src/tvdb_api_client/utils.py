from datetime import date, datetime

from tvdb_api_client.constants import DATE_FORMAT, DATETIME_FORMAT


def get_tvdb_date(date_string: str) -> date:
    if not date_string:
        return None

    return datetime.strptime(date_string, DATE_FORMAT).date()


def get_tvdb_datetime(datetime_string: str) -> datetime:
    if not datetime_string:
        return None

    return datetime.strptime(datetime_string, DATETIME_FORMAT)
