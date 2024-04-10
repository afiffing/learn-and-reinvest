import threading
import time
from collections import deque


class Printq:
    def __init__(self, initial=[], t=2):
        self.q = deque(initial)
        self.t = t
        threading.Timer(self.t, self.pq).start()

    def pq(self):
        if self.q:
            print(self.q.popleft())

        if self.q:
            threading.Timer(self.t, self.pq).start()

    def add(self, item):
        self.q.append(item)


q = Printq(list('123'))

while q.q:
    print("processing")
    time.sleep(1)