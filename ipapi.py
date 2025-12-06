
import requests


url = "https://ipapi.co/8.8.8.8/json/"
response = requests.get(url)

data = response.json()

print("Languages:", data["languages"])
