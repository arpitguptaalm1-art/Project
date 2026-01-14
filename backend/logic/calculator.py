def calculate_impact(decision_id):
    impact_map = {
        # ❌ BAD HABITS
        "D1": {"health": -3, "focus": -4, "career": -2},
        "D2": {"health": -1, "focus": -3, "career": -4},
        "D3": {"health": -2, "focus": -4, "career": -3},
        "D4": {"health": -4, "focus": -2, "career": -1},
        "D5": {"health": -3, "focus": -2, "career": -2},

        # ✅ GOOD HABITS
        "G1": {"health": 4, "focus": 3, "career": 2},
        "G2": {"health": 1, "focus": 4, "career": 5},
        "G3": {"health": 5, "focus": 2, "career": 1},
        "G4": {"health": 1, "focus": 3, "career": 4},
        "G5": {"health": 4, "focus": 2, "career": 2}
    }

    return impact_map.get(decision_id, {
        "health": 0,
        "focus": 0,
        "career": 0
    })