import os
import re

_valid_format = re.compile('[^:]+:[^:]+:[^:]+')


def _valid_line(line):
    """
    Check if a line is valid.

    A line is valid if it isn't a comment (comment are python style),
    and it is of the form "username:userkey:apikey".
    """
    if line.startswith('#'):
        return False

    return re.fullmatch(_valid_format, line)


def _valid_lines(secrets):
    with open(secrets) as secrets_file:
        lines = secrets_file.readlines()
        for line in filter(_valid_line, lines):
            yield line.strip()


def get_secrets_from_file(secrets):
    if not os.access(secrets, os.R_OK):
        return None

    for line in _valid_lines(secrets):
        username, userkey, apikey = line.split(':')
        return username, userkey, apikey
