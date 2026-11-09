import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not SERPER_API_KEY:
    raise SystemExit("Missing SERPER_API_KEY. Add it to the .env file in the repo root.")


def search_restaurants(postal_code):
    """Ask Serper Places for restaurants in a postal code area."""
    response = requests.post(
        "https://google.serper.dev/places",
        headers={"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"},
        json={"q": "restaurants Yonge and Sheppard North York", "location": "Toronto, Ontario, Canada", "gl": "ca"},
    )
    response.raise_for_status()
    return response.json().get("places", [])


if __name__ == "__main__":
    postal_code = "M2N"
    places = search_restaurants(postal_code)
    print(f"Found {len(places)} places for {postal_code}:\n")
    for place in places:
        print(f"- {place.get('title')} | {place.get('address')}")
