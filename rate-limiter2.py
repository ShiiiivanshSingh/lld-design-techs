# exponential Backoff

import time
import random
from functools import wraps

def retry(max_retry = 3, delay = 1.0, max_delay = 10.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retry):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retry -1:
                        raise

                    wait = min(delay * (2 ** attempt), max_delay)
                    jitter = random.uniform(0, wait * 0.1)
                    print(f"  retry {attempt + 1} failed, waiting {wait + jitter:.2f}s")
                    time.sleep(wait + jitter)
        return wrapper
    return decorator

@retry(max_retry=4, delay=2.0)
def fetch_bad():
    print("Attempting to fetch")
    raise ConnectionError("Service Unavailable")

if __name__ == "__main__":
    try:
        fetch_bad()
    except ConnectionError as e:
        print(f"Gave up: {e}")