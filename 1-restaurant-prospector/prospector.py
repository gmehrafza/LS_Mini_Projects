import csv
import os
import re
import unicodedata
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not SERPER_API_KEY:
    raise SystemExit("Missing SERPER_API_KEY. Add it to the .env file in the repo root.")

HEADERS = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}

CHAINS = [
    "cactus club", "joey", "earls", "the keg", "boston pizza", "kelseys",
    "montana's", "milestones", "jack astor", "mcdonald", "tim hortons",
    "starbucks", "subway", "pizza pizza", "a&w", "wendy", "burger king",
    "kfc", "popeyes", "chipotle", "five guys", "swiss chalet", "st-hubert",
]

PLATFORMS = {
    "ubereats.com": "Uber Eats",
    "doordash.com": "DoorDash",
    "skipthedishes.com": "SkipTheDishes",
}

GENERIC_WORDS = {"the", "restaurant", "bistro", "cafe", "bar", "grill", "kitchen",
                 "house", "and", "north", "york", "yonge", "toronto"}


def search_restaurants():
    """Ask Serper Places for restaurants near Yonge and Sheppard (M2N)."""
    response = requests.post(
        "https://google.serper.dev/places",
        headers=HEADERS,
        json={"q": "restaurants Yonge and Sheppard North York", "location": "Toronto, Ontario, Canada", "gl": "ca"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json().get("places", [])


def is_chain(name):
    """True if the restaurant name contains a known chain name."""
    name = name.lower()
    return any(chain in name for chain in CHAINS)


def clean_place(place):
    """Keep only the fields we need, with simple names."""
    return {
        "name": place.get("title", ""),
        "address": place.get("address", ""),
        "phone": place.get("phoneNumber", ""),
        "website": place.get("website", ""),
        "rating": place.get("rating", ""),
        "reviews": place.get("ratingCount", ""),
        "category": place.get("category", ""),
    }


def simplify(text):
    """Lowercase, remove accents (é -> e) and keep only letters and numbers."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9 ]", " ", text.lower())


def key_word(name):
    """The most distinctive word in the name, e.g. 'Grill Gate' -> 'gate'."""
    words = [w for w in simplify(name).split() if len(w) >= 3 and w not in GENERIC_WORDS]
    return words[0] if words else simplify(name).strip()


def check_platforms(name):
    """Search the 3 delivery sites and return the ones that list this restaurant."""
    query = f"{name} Toronto (site:ubereats.com OR site:doordash.com OR site:skipthedishes.com)"
    response = requests.post(
        "https://google.serper.dev/search",
        headers=HEADERS,
        json={"q": query, "gl": "ca", "num": 10},
        timeout=30,
    )
    response.raise_for_status()

    word = key_word(name)
    found = []
    for result in response.json().get("organic", []):
        link = result.get("link", "")
        text = simplify(result.get("title", "") + " " + link)
        for domain, label in PLATFORMS.items():
            if domain in link and word in text and label not in found:
                found.append(label)
    return found


if __name__ == "__main__":
    places = search_restaurants()
    restaurants = []
    for place in places:
        if is_chain(place.get("title", "")):
            print(f"Skipped chain: {place.get('title')}")
            continue
        restaurant = clean_place(place)
        platforms = check_platforms(restaurant["name"])
        restaurant["platforms"] = ", ".join(platforms) if platforms else "None found"
        restaurants.append(restaurant)

    print(f"\nChecked {len(restaurants)} independent restaurants:\n")
    for r in restaurants:
        print(f"- {r['name']} | {r['address']} | {r['platforms']}")

    output_file = Path(__file__).resolve().parent / "restaurants_M2N.csv"
    columns = ["name", "address", "phone", "website", "rating", "reviews", "category", "platforms"]
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(restaurants)
    print(f"\nSaved {len(restaurants)} restaurants to {output_file.name}")
