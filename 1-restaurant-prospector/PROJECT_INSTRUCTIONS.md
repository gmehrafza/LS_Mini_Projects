# 1 - Restaurant Prospector

## Purpose and status
Finds independent restaurants in a chosen Toronto postal code area (for example M2N) and checks whether each one is listed on Uber Eats, DoorDash or SkipTheDishes. Restaurants that are not on any platform become a prospect list for an online-ordering or delivery service, the same workflow I first built in Clay, rebuilt here in Python with the Serper API.

Status: In progress

## Requirements
- Input: a postal code prefix (e.g. M2N)
- Find independent restaurants in that area with the Serper API
- Check whether each one is listed on Uber Eats, DoorDash or SkipTheDishes
- Output: a CSV of restaurants

## Project structure
- prospector.py - main script

## Setup and run
From the repository root:
    pip3 install python-dotenv requests
    python3 1-restaurant-prospector/prospector.py

## Environment variables
- SERPER_API_KEY (Serper search), read from the root .env

## Known limitations

## Change log
- 2026-11-04: Project created
- 2026-11-09: Script loads SERPER_API_KEY from the root .env
