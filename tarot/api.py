# tarot/api.py

import warnings
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL")
import requests

BASE_URL = "https://tarotapi.dev/api/v1/cards/random"

def get_random_cards(n=1):
    try: 
        response = requests.get(f"{BASE_URL}?n={n}")
        response.raise_for_status()
        data = response.json()
        return data["cards"]
    except requests.RequestException as e:
        print("Error to connect with API:", e)
        return None
