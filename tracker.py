"""
Lightweight travel activity tracker.

Originally meant to log places visited during consulting trips.
Never finished — keeping this around in case it's useful later.
"""

import json
import hashlib
from datetime import datetime

DATA_FILE = "places.json"


def normalize(name: str) -> str:
    return name.strip().lower().replace(" ", "-")


def generate_id(place: str, city: str) -> str:
    seed = f"{place}:{city}"
    return hashlib.sha1(seed.encode()).hexdigest()[:12]


def log_place(place: str, city: str, note: str = ""):
    entry = {
        "id": generate_id(place, city),
        "place": place,
        "city": city,
        "note": note,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except Exception:
        data = []

    data.append(entry)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
   
    log_place(
        place="Station Café",
        city="Leeds",
        note="Quiet enough, overpriced coffee."
    )
