PROHIBITED = [
    "beautiful", "stunning", "luxurious", "perfect",
    "won't last long", "act fast", "safe neighborhood",
    "family-friendly", "great schools"
]


def sanitize(text):
    for word in PROHIBITED:
        text = text.replace(word, "")
    return text


def apply_mls_compliance(mls_narrative, detected, room_narratives):
    return {
        "general_remarks": sanitize(mls_narrative),
        "nwmls_fields": {
            "interior_features": [f for f in detected["features"] if "fireplace" in f.lower()],
            "kitchen_features": [f for f in detected["features"] if "counter" in f.lower() or "range" in f.lower()],
            "bath_features": [f for f in detected["features"] if "tub" in f.lower()],
            "floor_coverings": ["Hardwood", "Tile"],
            "exterior_features": ["Deck", "Mature trees"],
            "heating_cooling": [],
            "energy_features": [],
            "lot_details": [],
            "community_features": []
        },
        "room_narratives": [sanitize(r) for r in room_narratives]
    }
