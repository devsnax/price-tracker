import requests
import config

def fetch_price():
    url = config.URL
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    
    r = requests.get(url, params=params)
    data = r.json()
    return data["bitcoin"]["usd"]
