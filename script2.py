import requests
import json


url2 = "https://marine-api.open-meteo.com/v1/marine?latitude=-33.86&longitude=151.20&hourly=wind_speed_10m"


data2 = requests.get(url2).json()


print("SCRIPT 2 OUTPUT (Location 2 - Sydney)")
print(json.dumps(data2))


with open("location2.json", "w") as f:
    json.dump(data2, f, indent=4)

print("location2.json saved")
