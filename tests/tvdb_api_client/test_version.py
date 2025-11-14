from tvdb_api_client.__version__ import __version__


def test_version() -> None:
    assert isinstance(__version__, str)
    assert __version__[0].isdigit()
