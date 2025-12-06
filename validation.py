import json

# class with simple validation
class U:
    def _init_(self, data):
        self.a = data.get("A")
        self.b = data.get("B")

        if not isinstance(self.a, int):
            raise Exception("A must be an integer")

        if not isinstance(self.b, str):
            raise Exception("B must be a string")


def main():
    # read json file
    with open("output.json") as f:
        D = json.load(f)

    # counters
    valid = 0
    invalid = 0

    # loop through each item
    for item in D:
        try:
            obj = U(item)
            print("Valid:", obj.a, obj.b)
            valid += 1
        except Exception as e:
            print("Invalid:", item, "-", e)
            invalid += 1

    # summary
    print("\nSummary:")
    print("Valid:", valid)
    print("Invalid:", invalid)


main()