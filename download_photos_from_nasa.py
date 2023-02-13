import requests
import os
import pathlib
import datetime
from urllib.parse import urlparse

epic_images =[]
def download_epic_pics():
    epic_url = "https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY"
    response = requests.get(epic_url)
    response.raise_for_status()
    response_json = response.json()
    for record in response_json:
        epic_images.append(record['image'])

now = datetime.datetime.now()
download_epic_pics()
epic_urls =[]
for image in epic_images:
    picture =f'{image}.png'
    new_path = "/".join(['https://api.nasa.gov/EPIC/archive/natural',str(now.year),str(now.month),str(now.day),'png',picture])
    #print(new_path)
    new_url = f'{new_path}?api_key=DEMO_KEY'
    epic_urls.append(new_url)

for i, url in enumerate(epic_urls):
    filepath = 'nasa/'
    resp = requests.get(url)
    filename =(f'{filepath}/epic_{i}')
    with open(filename, 'wb') as file:
        file.write(resp.content)
