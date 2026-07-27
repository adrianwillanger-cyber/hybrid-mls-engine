def generate_mls_narrative(detected, market_data, address):
    return (
        f"Modern home at {address} featuring quartz surfaces, flat-panel cabinetry, "
        "stainless appliances, gas range, and natural light throughout."
    )


def generate_marketing_narrative(detected, market_data, address):
    return (
        f"This Northwest-modern home at {address} blends clean lines with warm materials. "
        "Quartz surfaces, a gas range, and a tree-lined deck create a calm, inviting feel."
    )


def generate_room_narratives(detected, room_map):
    narratives = []
    for photo in detected["photos"]:
        room = photo["room_type"]
        if "kitchen" in room:
            narratives.append("Kitchen with quartz counters, flat-panel cabinetry, and gas range.")
        if "bath" in room:
            narratives.append("Bath with freestanding soaking tub and tile flooring.")
    return narratives


def generate_social_copy(detected):
    return {
        "linkedin": "Modern NW home with quartz surfaces and natural light.",
        "instagram": "Bright kitchen, warm textures, private deck.",
        "facebook": "Contemporary design with thoughtful finishes."
    }


def generate_email_scripts(detected):
    return {
        "buyer": "Sharing a modern NW home with quartz surfaces and a private deck.",
        "sphere": "Just listed — clean, modern finishes and natural light.",
        "seller": "Your listing materials are ready and show beautifully."
    }


def generate_flyer_text(detected):
    return [
        "Modern Northwest design",
        "Quartz kitchen surfaces",
        "Gas range + stainless appliances",
        "Stone-faced fireplace",
        "Private deck",
        "Freestanding soaking tub"
    ]
