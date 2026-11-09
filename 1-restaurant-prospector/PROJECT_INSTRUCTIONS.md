# 1 - Restaurant Prospector

## Purpose and status
Finds independent restaurants in a chosen Toronto postal code area (for example M2N) and checks whether each one is listed on Uber Eats, DoorDash or SkipTheDishes. Restaurants that are not on any platform become a prospect list for an online-ordering or delivery service, the same workflow I first built in Clay, rebuilt here in Python with the Serper API.

Status: Done (v1)

## Requirements
- Find independent restaurants around Yonge & Sheppard (M2N) with the Serper Places API
- Skip known chains
- Check whether each one is listed on Uber Eats, DoorDash or SkipTheDishes
- Output: restaurants_M2N.csv

## Project structure
- prospector.py - main script
- requirements.txt - Python packages
- restaurants_M2N.csv - sample output from a real run
- README.md - project overview for readers

## Setup and run
From the repository root:
    pip3 install -r 1-restaurant-prospector/requirements.txt
    python3 1-restaurant-prospector/prospector.py

## Environment variables
- SERPER_API_KEY (Serper Places + Search), read from the root .env

## Known limitations
- Results vary between runs (Google returns slightly different places and links)
- "None found" is not proof; a restaurant may take orders elsewhere
- Chain list is manual
- No phone numbers from this Serper search
- Search area is fixed to Yonge & Sheppard

## Change log
- 2026-11-04: Project created
- 2026-11-09: Load SERPER_API_KEY from the root .env
- 2026-11-09: Search restaurants near Yonge & Sheppard, skip chains
- 2026-11-09: Check delivery platforms per restaurant
- 2026-11-09: Save results to CSV, add requirements.txt and README
