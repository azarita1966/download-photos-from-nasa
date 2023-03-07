import requests
from dotenv import load_dotenv
import os


def fetch_apod(file_path, api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key':api_key}
    response = requests.get(url, json=payload)
    response.raise_for_status()
    resp = response.content()["url"]
    os.makedirs(file_path, exist_ok=True)
    filename = f'{file_path}apod.jpg'
    with open(filename, 'wb') as file:
        file.write(resp)

if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ["NASA_KEY"]
    fetch_apod('images/', api_key)
