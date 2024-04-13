import requests, time


class clientRatelimiter:
    port = 5000
    api_url = f'http://localhost:{port}/api/v1/countries'


if __name__ == '__main__':
    cR = clientRatelimiter()

    for pings in range(0, 50):
        response = requests.get(cR.api_url)
        time.sleep(0.2)
        #response_json = response.content.decode().replace("'", '"')
        # print(
        #     f'Request number {pings}, Response status code: {response.status_code}, Content: {response_json}')
        print(
            f'Request number {pings}, Response status code: {response.status_code}, Content: {response.content}')