import json

data = [
    { "A": 2, "B": "a" },
    { "A": 3, "B": "b" },
    { "A": "x", "B": "c" },
    { "A": 5, "B": 10 },
    { "A": 6 },
    { "B": "d" },
    { "A": 7, "B": "e" }
]

# Save to a JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("JSON file saved as output1.json")
