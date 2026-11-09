# Restaurant Prospector

Finds independent restaurants around Yonge & Sheppard (Toronto, M2N) and checks whether each one is listed on **Uber Eats, DoorDash or SkipTheDishes**. Restaurants with no delivery platform become a prospect list for an online-ordering or delivery service.

I first built this workflow in **Clay** (Serper HTTP API + formula columns), then rebuilt it in **Python** to show the same GTM logic in code.

## How it works
1. **Find restaurants:** Serper Places API search around Yonge & Sheppard
2. **Remove chains:** skips names on a chain list (Cactus Club, JOEY, Landwer…)
3. **Check delivery platforms:** one Serper search per restaurant, limited to the 3 delivery sites with `site:`, and only counts a result if it mentions the restaurant's name
4. **Save results:** writes `restaurants_M2N.csv`

## Sample output
From a real run ([full file](restaurants_M2N.csv)):

| Restaurant | Address | Rating (reviews) | Delivery platforms |
|---|---|---|---|
| Grill Gate | 4907 Yonge St | 4.8 (1,900) | DoorDash, Uber Eats, SkipTheDishes |
| Han Ba Tang | 4862 Yonge St | 4.7 (2,300) | DoorDash, Uber Eats |
| Dum Pukht Yonge | 35 Sheppard Ave E | 4.7 (786) | DoorDash, Uber Eats |
| MeNami Udon & Izakaya | 5469 Yonge St | 4.5 (3,700) | Uber Eats |
| **Bistro Mujae** | 41 Spring Garden Ave | 4.8 (692) | **None found → prospect** |

## How to run
From the repository root:
```bash
pip3 install -r 1-restaurant-prospector/requirements.txt
python3 1-restaurant-prospector/prospector.py
```
Needs `SERPER_API_KEY` in the `.env` file at the repository root (see `.env.example`). Uses about 10 Serper credits per run.

## Known limitations
- **Results vary between runs.** Google returns slightly different restaurants and links each time, so a restaurant can be missed on one run (e.g. Grill Gate showed "None found" once).
- **"None found" is not proof.** The restaurant may take orders on its own website or another platform.
- **The chain list is manual.** New chains have to be added by hand.
- **No phone numbers.** This Serper search doesn't return them for these places.
- **Search area is fixed** to Yonge & Sheppard; other areas need a code change.

## Built with
Python · Serper API (Places + Search) · requests · python-dotenv