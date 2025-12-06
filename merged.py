import json

# Load the two JSON files
with open("location1.json") as f1:
    data1 = json.load(f1)

with open("location2.json") as f2:
    data2 = json.load(f2)

# Merge the data
merged = {
    "location1": data1,
    "location2": data2
}

# Save merged output
with open("merged_output.json", "w") as f:
    json.dump(merged, f, indent=4)

print("merged_output")
