from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from weather_api import get_today_weather
from main import export_csv

class WeatherBox(BoxLayout):
    def auto_update(self):
        city = self.ids.city_input.text.strip()
        weather = get_today_weather(city)
        if weather:
            date, temp, condition = weather
            self.ids.result.text = f"[b]{date}[/b]: {temp}°C, {condition}"
        else:
            self.ids.result.text = "❌ Could not fetch weather."

    def export(self):
        export_csv()
        self.ids.result.text = "✅ Exported to data.csv"

class WeatherApp(App):
    def build(self):
        return WeatherBox()

if __name__ == '__main__':
    WeatherApp().run()


