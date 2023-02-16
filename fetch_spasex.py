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
parser.add_argument('--series',
                    help = 'print series of the launch',
                    default = int(26))
args = parser.parse_args()

def fetch_spacex_launch(file_path):
    url='https://api.spacexdata.com/v5/launches/'
    payload = {'id':args.launch_id}
    response = requests.get(url, json=payload)
    response.raise_for_status()
    resp =response.json()[args.series]['links']['flickr']['original']
    for number, link in enumerate(resp):
        photo_link = requests.get(link)
        filename =(f'{file_path}/spacex_{number}.jpeg')
        with open(filename, 'wb') as file:
            file.write(photo_link.content)

if __name__ == '__main__':
    fetch_spacex_launch('new_spacex')

