# API

DRF endpoints under the `api` app, mounted at `/api/`. All are session/CSRF
auth with `AllowAny` permission unless noted.

| Method | Path              | Name         | Description                |
| ------ | ----------------- | ------------ | -------------------------- |
| GET    | `/api/health/`    | `health`     | Liveness probe             |
| GET    | `/api/stats/`     | `site-stats` | Public campaign stats      |
| GET    | `/api/donations/` | `donations`  | List of verified donations |
| GET    | `/api/charities/` | `charities`  | List of approved charities |

## GET `/api/health`

```json
{ "status": "ok" }
```

## GET `/api/stats/`

```json
{
  "verified_total": "0.00",
  "verified_count": 0,
  "goals_scored": 0
}
```

- `verified_total` — sum of `amount` across verified donations (string; DRF
  serializes `DecimalField` to preserve precision).
- `verified_count` — number of verified donations.
- `goals_scored` — from the hand-maintained `SiteStats` singleton.

## GET `/api/donations/`

All verified donations, most-recently-verified first.

```json
[
  {
    "id": 12,
    "created": "2026-06-04T18:30:00Z",
    "amount": "50.00",
    "name": "Sam R.",
    "charity": "Trevor Project"
  }
]
```

- `created` — when the donation was reported (ISO 8601).
- `amount` — donation amount (string; `DecimalField`, precision preserved).
- `name` — donor's display name, or `"Anonymous"` when left blank.
- `charity` — the attributed charity's name.

No PII (receipt file, verifier) is exposed.

## GET `/api/charities/`

All approved charities, alphabetical by name.

```json
[
  {
    "id": 3,
    "name": "Trevor Project",
    "url": "https://www.thetrevorproject.org/"
  }
]
```

- `name` — the charity's display name.
- `url` — the charity's website.
