# Author: Ashish Singh

import requests, time


class clientRatelimiter:

    def __init__(self):
        self.port = 80
        self.api_url = f'http://192.168.0.3:{self.port}'


if __name__ == '__main__':
    cR = clientRatelimiter()

    for pings in range(0, 50000000000000):
        response = requests.get(cR.api_url)
        time.sleep(0.2)
        #response_json = response.content.decode().replace("'", '"')
        # print(
        #     f'Request number {pings}, Response status code: {response.status_code}, Content: {response_json}')
        print(
            f'Request number {pings}, Response status code: {response.status_code}')
        with open("response.bin", "wb") as f:
            f.write(response.content)