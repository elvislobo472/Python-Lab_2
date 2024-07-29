from datetime import datetime, timedelta
import random

def gen_weath_data(start_date, end_date):
    weather_data = []
    current_date = start_date
    
    while current_date <= end_date:
        data = {
            "Date": current_date.strftime("%Y-%m-%d"),
            "Max Temp (°C)": random.randint(20, 35),
            "Min Temp (°C)": random.randint(15, 25),
            "Humidity (%)": random.randint(40, 80)
        }
        weather_data.append(data)
        current_date += timedelta(days=1)
    
    return weather_data

start_date = datetime(2023, 8, 1)
end_date = datetime(2024, 7, 10)

weather_data = gen_weath_data(start_date, end_date)


def temper(data):
    
    max_temp = max(day["Max Temp (°C)"] for day in data)
    min_temp = min(day["Min Temp (°C)"] for day in data)
    return max_temp, min_temp

def count_30(data):
    count = sum(1 for day in data if day["Max Temp (°C)"] > 30)
    return count

def avg_humid(data):
    
    tot_hum = sum(day["Humidity (%)"] for day in data)
    avg_humid = tot_hum / len(data)
    return avg_humid
