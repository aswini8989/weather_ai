import pandas as pd
from datetime import datetime
import os
from utils import validate_date, summarize_data
from weather_api import get_today_weather

DATA_FILE = 'data.csv'
date_set = set()

# Load existing data if file exists
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
    df['Date'] = pd.to_datetime(df['Date'])
    date_set = set(df['Date'].dt.strftime('%Y-%m-%d'))
else:
    df = pd.DataFrame(columns=['Date', 'Temperature', 'Condition'])

# Function to add manual weather data
def add_weather_data():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format!")
        return
    if date in date_set:
        print("Date already exists!")
        return
    try:
        temp = float(input("Enter temperature (°C): "))
        condition = input("Enter condition (e.g., Sunny, Rainy): ")

        global df
        df.loc[len(df)] = [date, temp, condition]
        date_set.add(date)
        print("✅ Weather data added.")
    except ValueError:
        print("Invalid temperature. Please enter a number.")

# Function to automatically add today's weather using API
def auto_update_today():
    weather = get_today_weather()
    if not weather:
        print("❌ Could not fetch weather.")
        return
    date, temp, condition = weather
    if date in date_set:
        print(f"⚠️ Weather for {date} already logged.")
        return
    global df
    df.loc[len(df)] = [date, temp, condition]
    date_set.add(date)
    print(f"✅ Auto-added: {date}, {temp}°C, {condition}")

# View full data
def view_data():
    print("\n📋 Weather Data:\n")
    print(df)

# Export to CSV
def export_csv():
    df.to_csv(DATA_FILE, index=False)
    print(f"✅ Data exported to {DATA_FILE}")

# Main loop
def main():
    while True:
        print("\n--- Weather Data Recorder ---")
        print("1. Add Weather Data (Manual)")
        print("2. View Data")
        print("3. View Summary (Weekly Average)")
        print("4. Export to CSV")
        print("5. Auto Update Today (From Internet)")
        print("6. Exit")
        print("7. Show Temperature Graph")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_weather_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            summarize_data(df)
        elif choice == '4':
            export_csv()
        elif choice == '5':
            auto_update_today()
        elif choice == '6':
            print("👋 Exiting. Have a nice day!")
        elif choice == '7':
            show_temperature_graph()
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")
def show_temperature_graph():
    import matplotlib.pyplot as plt
    if df.empty:
        print("No data to show.")
        return
    df_sorted = df.sort_values("Date")
    plt.plot(df_sorted['Date'], df_sorted['Temperature'], marker='o')
    plt.title("Daily Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
