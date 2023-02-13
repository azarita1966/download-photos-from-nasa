import requests
import os
import pathlib
import argparse

print(os.path.abspath(__file__))

parser = argparse.ArgumentParser("Launch id")

parser.parse_args()
parser.add_argument('--launch_id',
                    help = 'print ID of the launch',
                    default = ['5eb87d47ffd86e000604b38a'])

args = parser.parse_args()

def fetch_spacex_launch(file_path):
    url='https://api.spacexdata.com/v5/launches/'
    payload = {'id':args.launch_id}
    response = requests.get(url, json=payload)
    response.raise_for_status()
    json_resp =response.json()[31]['links']['flickr']['original']
    for i, link in enumerate(json_resp):
        resp = requests.get(link)
        filename =(f'{file_path}/spacex_{i}.jpeg')
        with open(filename, 'wb') as file:
            file.write(resp.content)

fetch_spacex_launch('new_spacex')

