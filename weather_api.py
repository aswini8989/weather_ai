import requests
from datetime import datetime

API_KEY = "20f37aea87e9f0714164faa306ab7e18"

def get_today_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return None
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        date = datetime.now().strftime("%Y-%m-%d")
        return date, temperature, condition
    except:
        return None

