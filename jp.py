import requests
import csv
from datetime import datetime, timedelta

# API的基本URL和您的API密鑰
base_url = "https://api.weatherapi.com/v1/history.json"
api_key = "88f42ed0256647fc915143845252003"

# 定義地點和日期範圍
location = "Fukuoka"
start_date = "2025-01-01"
end_date = "2025-03-20"

# 建立函數來呼叫API並獲取數據
def get_weather_data(location, date):
    url = f"{base_url}?key={api_key}&q={location}&dt={date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "date": date,
            "maxtemp_c": data["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
            "mintemp_c": data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
        }
    else:
        print(f"Error: {response.status_code}")
        return None

# 初始化變數
current_date = datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.strptime(end_date, "%Y-%m-%d")
weather_data = []

# 循環日期範圍並收集氣溫數據
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    data = get_weather_data(location, date_str)
    if data is not None:
        weather_data.append(data)
    current_date += timedelta(days=1)

# 將數據寫入CSV檔案
csv_file = "Fukuokaweather_data.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["date", "maxtemp_c", "mintemp_c"])
    writer.writeheader()
    writer.writerows(weather_data)

print(f"每日氣溫數據已保存到 {csv_file}")
