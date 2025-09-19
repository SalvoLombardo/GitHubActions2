import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, "appid": API_KEY, "units": "metric"}
    
    r = requests.get(url, params=params)
    data = r.json()

    if r.status_code != 200 or 'main' not in data:
        return {"error": data.get("message", "Impossibile recuperare dati")}

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }