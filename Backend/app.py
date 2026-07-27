from fastapi import FastAPI, UploadFile, Form

from models.feature_detection import detect_features
from models.compliance_filters import apply_mls_compliance
from models.narrative_generator import (
    generate_mls_narrative,
    generate_marketing_narrative,
    generate_room_narratives,
    generate_social_copy,
    generate_email_scripts,
    generate_flyer_text
)
from models.room_classifier import classify_rooms
from services.blob_storage import save_photo
from services.market_data import parse_market_csv

app = FastAPI(title="Hybrid Photo-to-MLS Narrative Engine")


@app.post("/process-listing")
async def process_listing(
    property_address: str = Form(...),
    photos: list[UploadFile] = Form(...),
    market_csv: UploadFile | None = None
):
    # Save photos
    photo_refs = [await save_photo(p) for p in photos]

    # Room classification
    room_map = classify_rooms(photo_refs)

    # Feature detection
    detected = detect_features(photo_refs, room_map)

    # Market data
    market_data = parse_market_csv(market_csv) if market_csv else None

    # Narrative generation
    mls_narrative = generate_mls_narrative(detected, market_data, property_address)
    marketing_narrative = generate_marketing_narrative(detected, market_data, property_address)
    room_narratives = generate_room_narratives(detected, room_map)
    social_copy = generate_social_copy(detected)
    email_scripts = generate_email_scripts(detected)
    flyer_text = generate_flyer_text(detected)

    # MLS compliance
    compliant = apply_mls_compliance(
        mls_narrative,
        detected,
        room_narratives
    )

    return {
        "property_address": property_address,
        "photos": detected["photos"],
        "detected_features": detected["features"],
        "market_data": market_data,
        "mls_general_remarks": compliant["general_remarks"],
        "nwmls_fields": compliant["nwmls_fields"],
        "room_narratives": compliant["room_narratives"],
        "marketing_narrative": marketing_narrative,
        "social_copy": social_copy,
        "email_scripts": email_scripts,
        "flyer_text": flyer_text
    }
