import json

with open("api_a.json") as f:
    api_a = json.load(f)
with open("api_b.json") as f:
    api_b = json.load(f)

required_a = ["user_id", "name", "device"]
required_b = ["location", "lat", "lon"]

for field in required_a:
    if field not in api_a:
        raise Exception(f"API A missing required field: {field}")

for field in required_b:
    if field not in api_b:
        raise Exception(f"API B missing required field: {field}")

dict_a = api_a
dict_b = api_b

aggregated = {
    "API_A_Result": dict_a,
    "API_B_Result": dict_b
}
print(json.dumps(aggregated, indent=4))
with open("aggregated_output.json", "w") as f:
    json.dump(aggregated, f, indent=4)
print("\nAggregated JSON saved as aggregated_output.json")
