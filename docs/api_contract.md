# API Contract

> Renamed from the original placeholder `appi-contact.md`.

## POST /process-listing

**Request** (`multipart/form-data`)

| Field | Type | Required |
|---|---|---|
| `property_address` | string | yes |
| `photos` | file[] | yes |
| `market_csv` | file | no |

**Response** (`application/json`)

See `Schema/dtask_engine_output.json` for the full shape. Top-level keys:

- `property_address`
- `photos`
- `detected_features`
- `market_data`
- `mls_general_remarks`
- `nwmls_fields` — see `Schema/nwmls_fields.json`
- `room_narratives`
- `marketing_narrative`
- `social_copy`
- `email_scripts`
- `flyer_text`
