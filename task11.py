import json
with open("file1.json") as f:
    data = json.load(f)
print(data[0]["frame"])