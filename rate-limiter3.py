# sliding window

import time
from functools import wraps


class RateLimitExceed(Exception):
    pass
class SlidingWinCounter:
    def __init__(self, limit =5, window_size_sec =60):
        self.limit = limit
        self.window = window_size_sec
        self.start = time.time() // self.window * self.window
        self.prev = self.cur = 0
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not self.allow():
                raise RateLimitExceed("Rate Limit Exceeded")
            return func(*args, **kwargs)
        return wrapper
    def allow(self):
        now = time.time()
        start = now // self.window * self.window

        if start > self.start:
            self.prev = self.cur if start - self.start == self.window else 0
            self.cur =0
            self.start = start
        weight = 1 - (now - start) / self.window
        count = self.cur + self.prev * weight

        if count >= self.limit:
            return 0
        self.cur += 1
        return 1

if __name__ == "__main__":
    rate_limiter = SlidingWinCounter(limit=3, window_size_sec=2)

    @rate_limiter
    def fetch_data(req_id):
        return f"Processed data {req_id}"

    print("--- Starting Rate Limiter Simulation ---")
    print("Limit: 3 requests per 2 seconds\n")

    for i in range(1, 9):
        current_time = f"{time.time():.2f}"[-5:]

        try:
            result = fetch_data(i)
            print(f"[T={current_time}] SUCCESS: {result}")
        except RateLimitExceed as e:
            print(f"[T={current_time}] BLOCKED: Request {i} - {e}")

        time.sleep(0.4)