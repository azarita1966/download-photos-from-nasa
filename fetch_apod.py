import requests
import argparse
from dotenv import load_dotenv

load_dotenv()
def fetch_apod(file_path):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key':os.environ.get("NASA_KEY")}
    response = requests.get(url, json=payload)
    response.raise_for_status()
    resp = response.content()["url"]
    filename =(f'{file_path}/apod.jpg')
    with open(filename, 'wb') as file:
        file.write(resp)

if __name__ == '__main__':
    fetch_apod('images/')
