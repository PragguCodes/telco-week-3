import time
from datetime import datetime

base_delay = 2
retries = 5

for attempt in range(1, retries + 1):
    wait = base_delay ** attempt
    print(f"\nAttempt {attempt}")
    before = datetime.now()
    print("Before wait:", before.strftime("%H:%M:%S"))
    time.sleep(wait)
    after = datetime.now()
    print("After wait :", after.strftime("%H:%M:%S"))
