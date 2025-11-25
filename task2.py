# Step 1: Use the same file made in previous task (import requests already done)
import requests

# Step 2: Create Custom Exception Class
class APIResponseError(Exception):
    """Exception to handle invalid API responses"""
    pass

# Step 3: Modify your network function to use custom exception
def fetch_data(url):
    try:
        print(f"\nFetching: {url}")
        response = requests.get(url, timeout=1)

        # Status code validation
        if response.status_code != 200:
            raise APIResponseError(f"Bad Status Code: {response.status_code}")

        # JSON validation
        try:
            response.json()
        except ValueError:
            raise APIResponseError("Invalid or Non-JSON Response")

        print("Success → Valid JSON received")

    except requests.exceptions.Timeout:
        print("Error → Timeout (server too slow)")

    except requests.exceptions.ConnectionError:
        print("Error → Host unreachable")

    # Step 4: Use custom exception inside try-except
    except APIResponseError as e:
        print(f"Custom Error → {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    finally:
        print("Request Completed")


# Step 5: Test with Good & Bad URLs
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://invalid.website.com",
    "https://httpstat.us/404",
    "https://google.com"
]

for url in urls:
    fetch_data(url)

print("\n---- Task 2 Completed ----")
