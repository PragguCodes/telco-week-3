import requests
import json
import yaml

# Step 1: Fetch JSON from a real API
resp = requests.get("https://jsonplaceholder.typicode.com/users")
json_data = resp.json()

# Step 2: Convert JSON to YAML
yaml_data = yaml.dump(json_data, sort_keys=False)

# Step 3: Save YAML file
with open("output.yaml", "w") as f:
    f.write(yaml_data)

print("Converted and saved to output.yaml")
