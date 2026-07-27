# Hybrid Photo-to-MLS Narrative Engine

A Northwest-modern, MLS-compliant listing engine that transforms property photos into:

- MLS General Remarks
- Full NWMLS Field Set
- Room-by-Room Narratives
- Marketing Narrative
- Social Copy
- Email Scripts
- Flyer/Brochure Text

This app combines:

- **Copilot Studio** (UI + workflow)
- **Azure Functions** (backend API)
- **Azure Blob Storage** (photo + log storage)
- **GitHub** (code + versioning)

---

## 🚀 Features

### 🔍 Vision + Feature Detection

Automatically identifies:

- Room types (kitchen, bath, living, exterior)
- Materials (quartz, tile, hardwood)
- Features (gas range, soaking tub, deck)
- Architectural elements (clerestory windows, built-ins)

### 🛡 MLS Compliance Engine

Auto-rewrites or removes:

- Subjective adjectives ("beautiful", "stunning")
- Puffery ("won't last long", "act fast")
- Fair-housing violations ("family neighborhood", "safe community")
- Buyer-targeting language ("perfect for investors")

### 🧠 Narrative Generator

Produces:

- MLS-compliant remarks
- Marketing narrative
- Room-by-room descriptions
- Social media copy
- Email scripts
- Flyer text

### 🗂 NWMLS Field Builder

Generates structured fields:

- Interior Features
- Kitchen Features
- Bath Features
- Floor Coverings
- Exterior Features
- Heating/Cooling
- Energy Features
- Lot Details
- Community Features

---

## 🧱 Project Structure

```
Backend/
  app.py                     FastAPI entrypoint — POST /process-listing
  config.py                  Environment-driven settings
  requirements.txt
  models/
    feature_detection.py     detect_features()
    compliance_filters.py    PROHIBITED list, sanitize(), apply_mls_compliance()
    narrative_generator.py   generate_*() narrative/copy functions
    room_classifier.py       classify_rooms() [stub — not from original convo]
  services/
    blob_storage.py          save_photo() — Azure Blob upload (stub)
    market_data.py           parse_market_csv() (stub)
    photo_processing.py      preprocess_photo() [stub — not from original convo]
Schema/
  nwmls_fields.json          JSON Schema for the NWMLS field set
  dtask_engine_output.json   JSON Schema for /process-listing's response
Branding/
  theme_token.json           Color/spacing tokens
  typography.json            Font tokens
docs/
  architecture.md            System flow (from notes/system map.docx)
  compliance_rules.md        Compliance engine rules + known gaps
  api_contract.md            /process-listing request/response contract
.github/workflows/
  deploy_to_azure.yml        CI/CD — deploys Backend/ to Azure Web App on push to main
notes/
  system map.docx            Original architecture diagram export
```

## Status

This is an early-stage scaffold. The functions above are placeholder
implementations pulled from an initial Copilot Studio planning conversation —
not production logic. See inline comments in `room_classifier.py` and
`photo_processing.py` for pieces that were stubbed in during setup rather
than pulled from that conversation.

## Local development

```bash
cd Backend
pip install -r requirements.txt
uvicorn app:app --reload
```

## Deployment

Pushing to `main` with changes under `Backend/` triggers
`.github/workflows/deploy_to_azure.yml`, which deploys to an Azure Web App
named `hybrid-mls-engine`. Requires an `AZURE_WEBAPP_PUBLISH_PROFILE` secret
set in the repo's GitHub Actions settings.
