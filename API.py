import requests  # Step 2

# Step 3 - Function to fetch API data
def fetch_data(url):
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
        data = response.json()
        print("Data received:", data)

    except requests.exceptions.Timeout:
        print(f"Timeout: Server took too long → {url}")

    except requests.exceptions.ConnectionError:
        print(f"Connection Error: Host unreachable → {url}")

    except requests.exceptions.JSONDecodeError:
        print(f"Invalid / Non-JSON response → {url}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e} → {url}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    finally:
        print("Request completed.\n")

# Step 5 - Testing with URLs
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",  # Valid
    "https://invalid.website12345.com",              # Host error
    "https://httpstat.us/404",                       # Status error
    "https://google.com"                             # Not JSON
]

for url in urls:
    fetch_data(url)
