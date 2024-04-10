# Author: Ashish Singh
# Rate limit X requests per Y seconds.
# Rate limiting is a threshold based setup. Sliding window is a threshold.
# Deque/double ended link lists are suitable for sliding windows.
# If X requests fits in sliding window of Y seconds, then it is allowed else rate-limited.

from collections import deque
import time


class Ratelimiter:

    # init is used to instantiate the object with arguments
    def __init__(self, maxRate, timeUnit):
        self.maxRate = maxRate
        self.timeUnit = timeUnit
        self.deque = deque(maxlen=maxRate)

    # call is used when object is called, r()
    def __call__(self):
        if len(self.deque) == self.deque.maxlen:
            currTime = time.time()
            if currTime - self.deque[0] > self.timeUnit:
                self.deque.append(currTime)
                return True
            else:
                return False
        self.deque.append(time.time())
        return True


if __name__ == '__main__':
    r = Ratelimiter(maxRate=5, timeUnit=1)
    for a in range(0, 100):
        time.sleep(0.1)
        print(a, 'Allowed requests' if r() else 'Rate-limited')
