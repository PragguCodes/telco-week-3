import yaml

with open("dockeryaml.yaml") as f:
    data = yaml.safe_load(f)

for service, details in data["services"].items():
    deps = details.get("depends_on", [])

    # convert list → comma-separated string
    if isinstance(deps, list):
        dep_list = ", ".join(deps)
    else:
        dep_list = "None"

    print(f"{service} -> {dep_list}")
