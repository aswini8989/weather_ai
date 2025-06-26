from datetime import datetime
import pandas as pd

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def summarize_data(df):
    if df.empty:
        print("No data to summarize.")
        return
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    weekly_avg = df['Temperature'].resample('W').mean()
    print("\nWeekly Average Temperature:")
    print(weekly_avg)
    df.reset_index(inplace=True)
