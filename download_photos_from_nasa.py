import requests
import os
import datetime
import dotenv


def get_epic_pics() -> list:
    #epic_images = []
    epic_url = "https://api.nasa.gov/EPIC/api/natural"
    params = {
        'api_key': os.environ.get("NASA_KEY"),
    }
    response = requests.get(epic_url, params=params)
    response.raise_for_status()
    resp = response.json()
    epic_images = [image['image'] for image in resp]
    return epic_images

def main_download():
    images = get_epic_pics()
    return images

def main_publish(images):
    now = datetime.datetime.now()
    for image in images:
        picture = f'{image}.png'
        new_url = "/".join(
            ['https://api.nasa.gov/EPIC/archive/natural', str(now.year), '02', '27', 'png',
             f'{picture}'])
        number = 0
        params = {
            'api_key': os.environ.get("NASA_KEY"),
        }
        resp = requests.get(new_url, params=params)
        resp.raise_for_status()
        os.makedirs('nasa', exist_ok=True)
        filepath = f'nasa/epic_{number}'
        with open(filepath, 'wb') as file:
            file.write(resp.content)
        number += 1


if __name__ == '__main__':
    dotenv.load_dotenv()
    images = main_download()
    main_publish(images)
