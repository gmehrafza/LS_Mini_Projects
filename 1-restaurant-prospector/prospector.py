import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not SERPER_API_KEY:
    raise SystemExit("Missing SERPER_API_KEY. Add it to the .env file in the repo root.")

print("Serper key loaded.")
