import yaml

with open("dockeryaml.yaml") as f:
    data = yaml.safe_load(f)

for env in data["services"]["oai-amf"]["environment"]:
    if "MCC=" in env:
        print(env.split("=")[1])
