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
        self.testApp = Flask(__name__)

        self.countries = [
            {'id': 1, 'country': 'India', 'capital': 'New Delhi'},
            {'id': 2, 'country': 'Indonesia', 'capital': 'New Delhi'},
        ]

    def serverStart(self):

        @self.testApp.get('/api/v1/countries')
        def get_countries():
            if len(self.deque) == self.deque.maxlen:
                currTime = time.time()
                if currTime - self.deque[0] > self.timeUnit:
                    self.deque.append(currTime)
                    return jsonify({'countries': self.countries})
                else:
                    self.testApp.logger.info("Rate-limited")
                    return Response("{'Reason':'Too many requests'}", status=429, mimetype='application/json')
            self.deque.append(time.time())
            return jsonify({'countries': self.countries})

    def run(self, debug_mode):
        self.serverStart()
        self.testApp.run(debug=debug_mode)


if __name__ == '__main__':
    r = Ratelimiter(maxRate=5, timeUnit=2)
    r.run(True)
