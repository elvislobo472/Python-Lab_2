from datetime import datetime
from mod_weather import temper, count_30, avg_humid, gen_weath_data

start_date = datetime(2023, 8, 1)
end_date = datetime(2024, 7, 10)


weather_data = gen_weath_data(start_date, end_date)

highest_temp, lowest_temp = temper(weather_data)
print(f"Highest Temperature Recorded: {highest_temp}°C")
print(f"Lowest Temperature Recorded: {lowest_temp}°C")

days_above_30 = count_30(weather_data)
print(f"Number of Days with Temperatures Above 30°C: {days_above_30}")

avg_humidity = avg_humid(weather_data)
print(f"Average Humidity: {avg_humidity:.2f}%")
