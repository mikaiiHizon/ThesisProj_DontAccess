import requests
import json
import os

# API Key and location
API_KEY = "6168fbba3a27d49df9cf44da2a6acd30"
CITY = "San Marcelino,PH"
CACHE_FILE = "weather_cache.json"

def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        # Try to get live data from the API
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "temp": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "status": "Online"
            }
            # Save for offline use
            with open(CACHE_FILE, "w") as f:
                json.dump(weather_data, f)
            return weather_data
    except:
        pass # If internet fails, move to the cache below

    #For Offline Mode
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cached = json.load(f)
            cached["status"] = "Offline (Cached)"
            return cached
    
    return {"temp": "N/A", "humidity": "N/A", "status": "No Signal"}