# weather_ai
# 🌤️ Stylish Weather Mobile App

An elegant weather application created using **Python** and **Kivy** framework. It fetches current weather data from the **OpenWeatherMap API**, exports it to a CSV file, and features a visually stylish UI with a lavender and peach green theme. Built with love and Times New Roman 💜

---

## 📦 Folder Contents

```
weather_mobile/
├── weather_mobile.py       # Main Python Kivy app
├── weather_mobile.kv       # Kivy UI layout (lavender + peach green)
├── weather_api.py          # Connects to OpenWeatherMap API
├── main.py                 # CSV export logic
```

---

## 🧰 Requirements

- Python 3.7+
- [Kivy](https://kivy.org/)
- Requests library

### 📥 Install Requirements

```bash
pip install kivy requests
```

---

## 🔑 OpenWeatherMap API Key

Your app uses a real-time weather API. The API key is already set in:

```python
# weather_api.py
API_KEY = "20f37aea87e9f0714164faa306ab7e18"
```

> Replace this with your own API key from [https://openweathermap.org/](https://openweathermap.org/) if needed.

---

## 🚀 How to Run

1. Unzip the folder:

```bash
unzip weather_mobile.zip
cd weather_mobile
```

2. Run the app:

```bash
python weather_mobile.py
```

3. Enter your city name and click the button to see weather details.

---

## 🧾 Features

- 📍 Get current weather (temperature & condition) by city name
- 🎀 Beautiful UI (Lavender background, Peach green input, Times New Roman font)
- 📤 Export data to CSV (prepares a sample row — customizable)
- 🔊 Voice & 📧 Email placeholders included (you can add these soon!)

---

## 📤 Export CSV

The **"Export Data to CSV"** button creates a `data.csv` file with sample values.  
You can modify `main.py` to log real weather values instead.

---

## 🛠️ Coming Soon (Ideas to Add)

- 🎤 Voice input using SpeechRecognition
- 📧 Send daily weather via email (SMTP)
- 📱 Convert to Android app using **Buildozer**
- 📊 Plot temperature graph using Matplotlib

---

## 👤 Author

**Aswini Viji**  
B.Tech IT | Python & Kivy Enthusiast  
Design-driven, passionate about creative UI and smart apps.

---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Free to use, learn from, and improve 💡

---

### 💜 Thank you for using Stylish Weather App 💜  
Let’s make weather feel beautiful!
