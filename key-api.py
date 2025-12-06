import requests
import json
url1 = "https://ipapi.co/8.8.8.8/json/"

url2 = "https://api.open-meteo.com/v1/wrong_endpoint"

try:
    response1 = requests.get(url1)
    print("Status Code:", response1.status_code)
    print("Final URL:", response1.url)
    data1 = response1.json()
    print("JSON Output:")
    print(json.dumps(data1, indent=4))
except Exception as e:
    print("Error:", e)


print("\n url-wrong")
try:
    response2 = requests.get(url2)
    print("Status Code:", response2.status_code)
    print("Final URL:", response2.url)
    data2 = response2.json()
    print(json.dumps(data2, indent=4))

except Exception as e:
    print("Error: Cannot get JSON for wrong URL")
    print("Exception:", e)
