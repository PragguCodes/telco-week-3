import requests
import json


url1 = "https://marine-api.open-meteo.com/v1/marine?latitude=25.76&longitude=-80.19&hourly=wave_height"


data1 = requests.get(url1).json()


print("SCRIPT 1 OUTPUT (Location 1 - Miami)")
print(json.dumps(data1))

with open("location1.json", "w") as f:
    json.dump(data1, f)

print("location1.json saved")
