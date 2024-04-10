from collections import deque
import time


class RateLimiter:
    def __init__(self, maxRate=5, timeUnit=1):
        self.timeUnit = timeUnit
        self.deque = deque(maxlen=maxRate)

    def __call__(self):
        if self.deque.maxlen == len(self.deque):
            cTime = time.time()
            if cTime - self.deque[0] > self.timeUnit:
                self.deque.append(cTime)
                return False
            else:
                return True
        self.deque.append(time.time())
        return False

r = RateLimiter()
for i in range(0,100):
    time.sleep(0.1)
    print(i, "block" if r() else "pass")


