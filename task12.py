import yaml

with open("student.yaml") as f:
    data = yaml.safe_load(f)
    print(data["skills"])
