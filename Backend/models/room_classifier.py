# NOTE: this file was not part of the original Copilot output — added as a
# minimal stub so app.py's `from models.room_classifier import classify_rooms`
# import resolves. Replace with a real vision-model call (Azure Computer
# Vision, a custom CV model, GPT-4V, etc.) before this goes to production.

ROOM_KEYWORDS = {
    "kitchen": ["kitchen", "range", "counter"],
    "bath": ["bath", "tub", "shower"],
    "living": ["living", "family room"],
    "exterior": ["exterior", "yard", "deck", "front"],
}


def classify_rooms(photo_refs):
    """
    Placeholder room classifier. Guesses room type from filename hints
    in each photo reference. Returns {photo_ref: room_type}.
    """
    room_map = {}
    for ref in photo_refs:
        lowered = ref.lower()
        matched = "other"
        for room, keywords in ROOM_KEYWORDS.items():
            if any(kw in lowered for kw in keywords):
                matched = room
                break
        room_map[ref] = matched
    return room_map
