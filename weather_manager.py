import requests
import json
import os
from datetime import datetime

# API Key and location
API_KEY = "6168fbba3a27d49df9cf44da2a6acd30"
CITY = "San Marcelino,PH"
CACHE_FILE = "weather_cache.json"
FORECAST_CACHE = "forecast_cache.json"

def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "temp": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "status": "Online"
            }
            with open(CACHE_FILE, "w") as f:
                json.dump(weather_data, f)
            return weather_data
    except:
        pass

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cached = json.load(f)
            cached["status"] = "Offline (Cached)"
            return cached
    
    return {"temp": "N/A", "humidity": "N/A", "status": "No Signal"}

def get_forecast_data():
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            api_data = response.json()
            forecast = parse_forecast(api_data['list'])
            full_data = {
                'current': get_weather_data().copy(),
                'forecast': forecast
            }
            with open(FORECAST_CACHE, "w") as f:
                json.dump(full_data, f)
            return full_data
    except:
        pass

    if os.path.exists(FORECAST_CACHE):
        with open(FORECAST_CACHE, "r") as f:
            return json.load(f)
    
    return {'current': get_weather_data(), 'forecast': {'days': []}}

def parse_forecast(hourly_list):
    # Group by day
    day_groups = {}
    today_str = datetime.now().strftime('%Y-%m-%d')
    tomorrow_str = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    day3_str = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    
    day_names = [today_str, tomorrow_str, day3_str]
    
    for entry in hourly_list:
        dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
        date_str = dt.strftime('%Y-%m-%d')
        
        if date_str in day_names:
            day_idx = day_names.index(date_str)
            if day_idx not in day_groups:
                day_groups[day_idx] = {'hours': [], 'temps': [], 'mains': [], 'hum': []}
            day_groups[day_idx]['hours'].append({
                'time': dt.strftime('%H:00'),
                'temp': round(entry['main']['temp']),
                'cond': entry['weather'][0]['main'],
                'icon': entry['weather'][0]['icon']
            })
            day_groups[day_idx]['temps'].append(entry['main']['temp'])
            day_groups[day_idx]['mains'].append(entry['weather'][0]['main'])
            day_groups[day_idx]['hum'].append(entry['main']['humidity'])
    
    days = []
    day_labels = ['Today', 'Tomorrow', 'Day After']
    
    for i in range(3):
        if i in day_groups:
            group = day_groups[i]
            avg_temp = round(sum(group['temps']) / len(group['temps']))
            cond_count = max(set(group['mains']), key = group['mains'].count)
            days.append({
                'date': day_labels[i],
                'summary': f"{cond_count.title()} {avg_temp}°C avg",
                'hours': group['hours'][:8]  # First 8 hours (24h/3h=8)
            })
    
    return {'days': days}

from datetime import timedelta, datetime

