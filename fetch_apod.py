import requests
import argparse

parser = argparse.ArgumentParser("api_key")

parser.parse_args()
parser.add_argument('--my_api_key',
                    help = 'print your api key',
                    default = ['DEMO_KEY'])

args = parser.parse_args()


def fetch_apod(file_path):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key':args.my_api_key}
    response = requests.get(url, json=payload)
    response.raise_for_status()
    resp = response.content()["url"]
    filename =(f'{file_path}/apod.jpg')
    with open(filename, 'wb') as file:
        file.write(resp)
fetch_apod('images/')
