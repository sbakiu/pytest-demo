import requests


def get_json(url: str):
    response = requests.get(url)
    return response.json()
