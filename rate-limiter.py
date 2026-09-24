# token bucket

import time

class RateLimiter:
    def __init__(self, capacity: int, refill_rps: float):
        self.capacity = capacity
        self.refill_rate = refill_rps
        self.token = float(capacity)
        self.last_check = time.monotonic()
    
    def allow_request(self) ->bool:
        now = time.monotonic()
        time_passed = now - self.last_check

        self.token = min(self.capacity, self.token + (time_passed * self.refill_rate))
        self.last_check = now

        if self.token >= 1.0:
            self.token -= 1.0
            return True
        return False
    
limiter = RateLimiter(capacity=5, refill_rps=2.0)


if __name__ == "__main__":
    print([limiter.allow_request() for _ in range(7)])
    time.sleep(1)
    print(limiter.allow_request())