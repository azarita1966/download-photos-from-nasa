import requests
import os
import pathlib
import datetime
from dotenv import load_dotenv

load_dotenv()

def get_epic_pics_list():
    epic_images = []
    epic_url = "https://api.nasa.gov/EPIC/api/natural"
    params= {
        'api_key':os.environ.get("NASA_KEY")}
    response = requests.get(epic_url, params = params)
    response.raise_for_status()
    resp = response.json()
    epic_images=[image['image'] for image in resp]
    return epic_images

def main():
    images = get_epic_pics_list()
    now = datetime.datetime.now()
    epic_urls =[]
    for image in images:
        picture =f'{image}.png'
        new_url = "/".join(['https://api.nasa.gov/EPIC/archive/natural',str(now.year),str(now.month),str(now.day-1),'png',f'{picture}'])
        epic_urls.append(new_url)
    for number, url in enumerate(epic_urls):
        directory = 'nasa/'
        params = {
            'api_key':os.environ.get("NASA_KEY")}
        resp = requests.get(url, params = params)
        resp.raise_for_status()
        filepath =(f'{directory}/epic_{number}')
        with open(filepath, 'wb') as file:
            file.write(resp.content)

if __name__ == '__main__':
    main()

