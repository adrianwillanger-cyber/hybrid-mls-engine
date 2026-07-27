def detect_features(photo_refs, room_map):
    features = []
    materials = []
    photos_out = []

    for ref in photo_refs:
        room = room_map[ref]
        # Example placeholder logic
        if "kitchen" in room:
            features.extend(["Quartz countertops", "Gas range", "Stainless appliances"])
            materials.extend(["Quartz", "Tile", "Painted wood"])
        if "bath" in room:
            features.extend(["Freestanding soaking tub", "Tile flooring"])
            materials.extend(["Tile"])

        photos_out.append({
            "id": ref,
            "room_type": room,
            "features": features,
            "materials": materials
        })

    return {
        "photos": photos_out,
        "features": list(set(features)),
        "materials": list(set(materials))
    }
