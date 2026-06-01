# Usage

The central object is the `TheTVDBClient` client which needs the
`api_key` supplied by the [TheTVDB]. It can be initialised with a
cache (optionally), and if no cache is passed a dummy cache object
will be created.

???+ tip "Cache"

    It is advisable to use a cache that will persist during a server
    restart, so that the token will not have to be regenerated.

!!! danger "Security warning"

    Please be advised that the token will be stored in the default
    cache in plaintext, so if there are any security considerations
    they should be taken care into account when choosing the cache.

## Configuration

You can provide credentials in any of these ways (checked in this order):

1. **Direct constructor argument** — pass `api_key` (and optionally `pin`) to `TheTVDBClient`.
2. **Environment variables** — set `TVDB_API_KEY_V4` and/or `TVDB_PIN_V4`.
3. **Config file** — create `the_tvdb.yaml` in `$XDG_CONFIG_HOME` with a `client` section:

```yaml
client:
    api_key: your-api-key
    pin: your-pin # optional
```

!!! danger "Security warning"

    Passing secrets in env vars is insecure, as some operating systems
    allow non-root users to see process environment variables via `ps`.
    It is advised to use the config file option and set restrictive
    permissions on it (e.g. `chmod 600 the_tvdb.yaml`).

## The TVDB API Client

???+ tip "Refreshing cache"

    All methods use the cached value when present.
    Pass `refresh_cache=True` to any of them to fetch fresh data.

### `get`

```python
def get(path: str) -> dict[str, object]
```

Low-level method that performs an authenticated GET request to the TVDB API and
returns the raw JSON response. Use the higher-level methods below unless you need
an endpoint not yet wrapped by this client.

```python
data = client.get("series/81189")
```

### `get_series_by_id`

```python
def get_series_by_id(tvdb_id: int, *, refresh_cache: bool = False) -> Series
```

Fetches a TV series by its TVDB id and returns a parsed `Series` object.

```python
series = client.get_series_by_id(81189)
print(series.name)          # "Breaking Bad"
print(series.status.name)   # "Ended"
print(series.first_aired)   # datetime.date(2008, 1, 20)
```

### `get_raw_series_by_id`

```python
def get_raw_series_by_id(tvdb_id: int, *, refresh_cache: bool = False) -> SeriesRawData
```

Same as `get_series_by_id` but returns the raw API dict instead of a `Series`
dataclass. Useful when you need fields not yet exposed by the data model.

```python
raw = client.get_raw_series_by_id(81189)
print(raw["name"])  # "Breaking Bad"
```

### `get_episodes_by_series`

```python
def get_episodes_by_series(
    tvdb_id: int,
    season_type: str = "default",
    *,
    refresh_cache: bool = False,
) -> list[Episode]
```

Fetches all episodes for a TV series and returns a list of parsed `Episode`
objects. Handles pagination automatically.

```python
episodes = client.get_episodes_by_series(81189)
for ep in episodes:
    print(ep.season_number, ep.number, ep.name)
```

The `season_type` parameter controls the ordering used by TVDB:

| Value         | Description                                     |
| ------------- | ----------------------------------------------- |
| `"default"`   | The series' default ordering (usually official) |
| `"official"`  | Broadcast / official season ordering            |
| `"dvd"`       | DVD release ordering                            |
| `"absolute"`  | Absolute (continuous) episode numbering         |
| `"alternate"` | Alternate ordering defined by the community     |
| `"regional"`  | Region-specific ordering                        |

### `get_raw_episodes_by_series`

```python
def get_raw_episodes_by_series(
    tvdb_id: int,
    season_type: str = "default",
    page: int = 0,
    *,
    refresh_cache: bool = False,
) -> CleanedEpisodeData
```

Same as `get_episodes_by_series` but returns raw dicts and exposes the `page`
parameter for manual pagination. Each page contains up to 500 episodes.

```python
page = client.get_raw_episodes_by_series(81189, page=0)
print(page["has_next_page"])  # False for most series
```

## Data Models

### `Series`

| Field                   | Type               | Description                               |
| ----------------------- | ------------------ | ----------------------------------------- |
| `id`                    | `int`              | TVDB series id                            |
| `name`                  | `str`              | Primary title                             |
| `slug`                  | `str`              | URL-friendly identifier                   |
| `image`                 | `URL \| None`      | Poster image URL                          |
| `name_translations`     | `list[str]`        | Language codes with a translated title    |
| `overview_translations` | `list[str]`        | Language codes with a translated overview |
| `aliases`               | `list[Alias]`      | Alternative titles                        |
| `first_aired`           | `date \| None`     | Date the series first aired               |
| `last_aired`            | `date \| None`     | Date the series last aired                |
| `next_aired`            | `date \| None`     | Date of the next episode                  |
| `score`                 | `float`            | Community rating score                    |
| `status`                | `Status`           | Current airing status                     |
| `original_country`      | `str`              | Country of origin                         |
| `original_language`     | `str`              | Original language                         |
| `default_season_type`   | `int`              | Default season ordering id                |
| `is_order_randomized`   | `bool`             | Whether episode order is randomised       |
| `last_updated`          | `datetime \| None` | Last metadata update timestamp            |
| `average_runtime`       | `int`              | Average episode runtime in minutes        |
| `overview`              | `str`              | Plot summary                              |

### `Episode`

| Field                   | Type               | Description                                         |
| ----------------------- | ------------------ | --------------------------------------------------- |
| `id`                    | `int`              | TVDB episode id                                     |
| `series_id`             | `int`              | TVDB id of the parent series                        |
| `name`                  | `str`              | Episode title                                       |
| `aired`                 | `date \| None`     | Air date                                            |
| `runtime`               | `int`              | Runtime in minutes                                  |
| `name_translations`     | `list[str]`        | Language codes with a translated title              |
| `overview`              | `str`              | Episode synopsis                                    |
| `overview_translations` | `list[str]`        | Language codes with a translated overview           |
| `image`                 | `URL \| None`      | Episode still image URL                             |
| `image_type`            | `int`              | Image type code                                     |
| `is_movie`              | `int`              | Non-zero if this is a movie entry                   |
| `number`                | `int`              | Episode number within its season                    |
| `season_number`         | `int`              | Season number                                       |
| `last_updated`          | `datetime \| None` | Last metadata update timestamp                      |
| `finale_type`           | `str`              | Finale classification (e.g. `"season"`, `"series"`) |

### `Status`

| Field          | Type   | Description                                            |
| -------------- | ------ | ------------------------------------------------------ |
| `id`           | `int`  | Status id                                              |
| `name`         | `str`  | Human-readable status (e.g. `"Ended"`, `"Continuing"`) |
| `record_type`  | `str`  | Record type this status applies to                     |
| `keep_updated` | `bool` | Whether TVDB continues updating this record            |

### `Alias`

| Field      | Type  | Description                        |
| ---------- | ----- | ---------------------------------- |
| `language` | `str` | BCP 47 language code               |
| `name`     | `str` | Alternative title in that language |

[TheTVDB]: https://thetvdb.com/api-information
