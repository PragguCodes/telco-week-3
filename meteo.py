import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m,pressure_msl,wind_speed_10m"

response = requests.get(url)

data = response.json()

print("JSON Data:")
print(data)
