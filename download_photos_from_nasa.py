import requests
import os
import datetime
from dotenv import load_dotenv
from pathlib import Path


def download_image(url, file_name, folder='images'):
    response = requests.get(url)
    response.raise_for_status()
    os.makedirs(folder, exist_ok=True)
    with open(Path.cwd() / folder / file_name, 'wb') as file:
        file.write(response.content)


def get_nasa_request(url, nasa_key):
    params = {
        'api_key': nasa_key,
        }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_epic_pics(nasa_key, natural=True, folder='epics'):
    if natural:
        collection = 'natural'
    else:
        collection = 'enhanced'
    epic_url = "https://api.nasa.gov/EPIC/api/natural"
    for image in get_nasa_request(epic_url, nasa_key):
        image_name = image['image']
        datetime_date = datetime.datetime.strptime(image['date'],'%Y-%m-%d %H:%M:%S')
        image_date = datetime_date.strftime('%Y/%m/%d')
        image_link = f'https://epic.gsfc.nasa.gov/archive/{collection}'
        image_link = f'{image_link}/{image_date}/png/{image_name}.png'
        file_name = f'{image_name}.png'
        download_image(image_link, file_name= file_name, folder = folder)


if __name__ == '__main__':
    load_dotenv()
    nasa_key = os.environ["NASA_KEY"]
    get_epic_pics(nasa_key)
