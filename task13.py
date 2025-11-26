import yaml

with open("dockeryaml.yaml") as f:
    data = yaml.safe_load(f)
    print(data["services"])
