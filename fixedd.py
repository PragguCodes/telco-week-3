import time
from datetime import datetime

FIXED_DELAY = 2
RETRIES = 5

for attempt in range(1, RETRIES + 1):
    print(f"\nAttempt {attempt}")
    before = datetime.now()
    print("Before wait :", before.strftime("%H:%M:%S"))
    time.sleep(FIXED_DELAY)
    after = datetime.now()
    print("After wait  :", after.strftime("%H:%M:%S"))
