import requests, json, time


class clientRatelimiter:
    port = 5000
    api_url = f'http://localhost:{port}/api/v1/countries'


if __name__ == '__main__':
    cR = clientRatelimiter()

    for pings in range(0, 100):
        time.sleep(0.2)
        try:
            response = requests.get(cR.api_url)
            # print(f'Request number {pings}, Response status code: {response.status_code}, Response: {json.dumps(response.json())}')
            print(f'Request number {pings}, {response.raise_for_status()}', {response.status_code})
        except requests.exceptions.HTTPError as err:
            print(f'Request number {pings},{err}')
            continue
