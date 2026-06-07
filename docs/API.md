# API

DRF endpoints under the `api` app, mounted at `/api/`. All are session/CSRF
auth with `AllowAny` permission unless noted.

| Method | Path           | Name         | Description           |
| ------ | -------------- | ------------ | --------------------- |
| GET    | `/api/health/` | `health`     | Liveness probe        |
| GET    | `/api/stats/`  | `site-stats` | Public campaign stats |

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
