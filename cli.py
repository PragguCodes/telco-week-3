import os


def test_ip():
    ip_list = ["8.8.8.8", "1.1.1.1"]
    for ip in ip_list:
        print("Checking {ip} ...")
        response = os.system(f"ping -n 1 {ip} > nul")
        if response == 0:
            print("{ip} is reachable ✔")
        else:
            print("{ip} is not reachable ✖")


def latency_summary():
    values = input("Enter latencies (comma-separated): ")
    nums = [int(x) for x in values.split(",")]

    print("\nLatency Summary:")
    print("Min =", min(nums))
    print("Max =", max(nums))
    print("Avg =", sum(nums) / len(nums))


while True:
    print(" MENU ")
    print("1. Test IP Reachability")
    print("2. Latency Summary")
    print("3. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        test_ip()
    elif ch == "2":
        latency_summary()
    elif ch == "3":
        print("Bye")
        break
    else:
        print("Invalid Option Try again")
