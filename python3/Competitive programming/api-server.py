# Rate limiiter is a threshold based problem statement
# sliding window is a threshold
# X requests fits in sliding window of Y seconds
import time

from flask import Flask, jsonify, Response
from collections import deque


class Ratelimiter:

    def __init__(self, maxRate, timeUnit):
        self.maxRate = maxRate
        self.timeUnit = timeUnit
        self.deque = deque(maxlen=maxRate)
        self.app = Flask(__name__)

        self.countries = [
            {'id': 1, 'country': 'India', 'capital': 'New Delhi'},
            {'id': 2, 'country': 'Indonesia', 'capital': 'New Delhi'},
        ]

    def serverStart(self):

        @self.app.get('/api/v1/countries')
        def get_countries():
            if len(self.deque) == self.deque.maxlen:
                currTime = time.time()
                if currTime - self.deque[0] > self.timeUnit:
                    self.deque.append(currTime)
                    return jsonify({'countries': self.countries})
                else:
                    return Response("{'Reason':'Too Many requests'}", status=429, content_type='application/json')
            self.deque.append(time.time())
            return jsonify({'countries': self.countries})

    def run(self, debug_mode):
        self.serverStart()
        self.app.run()


if __name__ == '__main__':
    r = Ratelimiter(maxRate=5, timeUnit=2) #5 Requests per 2 seconds
    r.run(True)
