
import requests

url = "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}"
response = requests.get(url)

data = response.json()

print("JSON Data:")
print(data)
