import requests, time
from concurrent.futures import ThreadPoolExecutor, as_completed
import uuid


class clientRatelimiter:

    def __init__(self):
        self.port = 5000
        self.api_url = f'http://localhost:{self.port}/api/v1/countries'

    def get_response(self):
        for pings in range(0, 10):
            time.sleep(1)
            response = requests.get(self.api_url)
            print(uuid.uuid4(), f'Request number {pings}, Response status code: {response.status_code}')
        #return response.status_code

    def threadRunner(self):
        threads = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            print(executor.submit(self.get_response()))
            #time.sleep(5)
            print("slept for 1 sec")
            self.get_response()


if __name__ == '__main__':
    cR = clientRatelimiter()
    cR.threadRunner()

    # threads = []
    # response = requests.get(cR.api_url)
    # with ThreadPoolExecutor(max_workers=20) as executor:
    #     print(executor)
    # threads.append(executor.submit(response))
    #
    # for task in as_completed(threads):
    #     print(task.result())

    # for pings in range(0, 50):
    #     response = requests.get(cR.api_url)
    #     time.sleep(0.2)
    #     # response_json = response.content.decode().replace("'", '"')
    #     # print(
    #     #     f'Request number {pings}, Response status code: {response.status_code}, Content: {response_json}')
    #     print(
    #         f'Request number {pings}, Response status code: {response.status_code}, Content: {response.content}')
