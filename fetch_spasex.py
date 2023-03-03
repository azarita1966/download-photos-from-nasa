import requests
import os
import argparse


def fetch_spacex_launch(launch_id, folder ='new_spasex'):
    url = 'https://api.spacexdata.com/v5/launches/'
    payload = {'id': launch_id}
    response = requests.get(url, json=payload)
    response.raise_for_status()
    resp = response.json()[args.series]['links']['flickr']['original']
    for number, link in enumerate(resp):
        photo_link = requests.get(link)
        photo_link.raise_for_status()
        os.makedirs(folder, exist_ok=True)
        filename = f'{folder}/launch_{number}.jpeg'
        with open(filename, 'wb') as file:
            file.write(photo_link.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id',
                        help='print ID of the launch',
                        type =int,
                        default=10)
    parser.add_argument('--series',
                        help='print series of the launch',
                        default=int(26))
    args = parser.parse_args()
    print(f"\n{args.launch_id} -th launch. Getting urls of the spasex images")
    fetch_spacex_launch(args.launch_id)
