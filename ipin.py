
import requests

url = "https://api.ipinfo.io/lite/8.8.8.8?token=3db06ae49bc7e3"
response = requests.get(url)

data = response.json()

print("JSON Data:")
print(data)
