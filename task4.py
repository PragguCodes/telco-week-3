import requests
import logging

# Step 3: Logging settings
logging.basicConfig(
    filename="decorator_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 3: Create a decorator to auto-log function calls
def auto_log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function Called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# Step 2: Implement API function
@auto_log   # Step 4: Apply decorator
def fetch_data(url):
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
        return "Success: Data received"
    except Exception as e:
        return f"Error Occurred: {e}"


# Step 5: Testing
print(fetch_data("https://jsonplaceholder.typicode.com/posts/1"))
print(fetch_data("https://invalid.website.com"))
print(fetch_data("https://httpstat.us/404"))

print("\n--- Task 4 Completed ---")
print("Check decorator_log.txt for auto-logs")
