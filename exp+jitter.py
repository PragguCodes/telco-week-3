import time
import random
from datetime import datetime

base_delay = 2
retries = 5
timestamps = []

for attempt in range(1, retries + 1):
    wait = (base_delay ** attempt) + random.uniform(0, 1)
    before = datetime.now()
    time.sleep(wait)
    after = datetime.now()
    timestamps.append((attempt, round(wait, 2), before, after))

for att, w, b, a in timestamps:
    print(f"Attempt {att} | Wait: {w}s | Before: {b.strftime('%H:%M:%S')} | After: {a.strftime('%H:%M:%S')}")
