import requests

worker_url = "your worker url"

def send_request(url, method='GET', headers=None, data=None, cookies=None) -> requests.models.Response:
    params = {
        'url': url,
        'method': method
    }

    if headers:
        params['headers'] = str(headers)

    if data:
        params['data'] = str(data)

    if cookies:
        params['cookies'] = str(cookies)

    response = requests.get(worker_url, params=params)
    print(type(response))
    return response

if __name__ == "__main__":
    print(send_request("https://www.aparat.com").text)