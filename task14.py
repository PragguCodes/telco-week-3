import yaml

with open("dockeryaml.yaml") as f:
    data = yaml.safe_load(f)

for service, details in data["services"].items():
    try:
        ip = details["networks"]["public_net"]["ipv4_address"]
        print(service, "->", ip)
    except:
        print(service, "-> No IP assigned")
