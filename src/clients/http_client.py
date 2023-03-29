import requests


class HttpClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token

    def post(self, url: str, body):
        headers = {}
        if self.token is not None and self.token != "":
            headers["Authorization"] = f"Bearer {self.token}"

        response = requests.post(f"{self.base_url}{url}", json=body, headers=headers)

        if response.status_code <= 299:
            return response.json()

        raise Exception(response.status_code)
