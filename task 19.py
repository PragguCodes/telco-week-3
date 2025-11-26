import subprocess
import json

# Get routing table lines
routes = subprocess.check_output("route_table.json", shell=True).decode().splitlines()

result = []

for line in routes:
    parts = line.split()
    entry = {"route": parts[0]}   # first word is always route prefix

    # scan all words
    for i in range(len(parts)):
        if parts[i] == "via":
            entry["gateway"] = parts[i+1]
        if parts[i] == "dev":
            entry["interface"] = parts[i+1]
        if parts[i] == "proto":
            entry["protocol"] = parts[i+1]
        if parts[i] == "src":
            entry["source"] = parts[i+1]
        if parts[i] == "metric":
            entry["metric"] = parts[i+1]

    result.append(entry)

print(json.dumps(result, indent=4))
