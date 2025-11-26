import requests

url = "https://jsonplaceholder.typicode.com/users"

resp = requests.get(url)
data = resp.json()

print(data[0])
