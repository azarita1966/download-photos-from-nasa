import requests
import os
import pathlib
import datetime
from urllib.parse import urlparse

epic_images =[]
def download_epic_pics():
    epic_url = "https://api.nasa.gov/EPIC/api/natural"
    headers = {
        "api_key": 'DEMO_KEY'}
    response = requests.get(epic_url, headers=headers)
    response.raise_for_status()
    resp = response.json()
    for image in resp:
        epic_images = [image['image'] for image in resp]
    return epic_images

def main():
    epic_images = download_epic_pics()
    now = datetime.datetime.now()
    epic_urls =[]
    for image in epic_images:
        picture =f'{image}.png'
        new_url = "/".join(['https://api.nasa.gov/EPIC/archive/natural',str(now.year),'02','15','png',picture])
        epic_urls.append(new_url)

    for number, url in enumerate(epic_urls):
        directory = 'nasa/'
        headers = {
            "api_key": 'DEMO_KEY'}
        resp = requests.get(url, headers = headers)
        response.raise_for_status()
        filepath =(f'{directory}/epic_{number}')
        with open(filepath, 'wb') as file:
            file.write(resp.content)

if __name__ == '__main__':
    main()

