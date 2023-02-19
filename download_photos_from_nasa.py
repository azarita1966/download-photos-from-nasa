import requests
import os
import pathlib
import datetime
import telegram
import argparse
import time
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

    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN']
    print(bot.get_me())
    updates = bot.get_updates()
    print(updates[0])
    chat_id = updates[-1].message.chat_id
    bot.send_message(text='Hi Alina!', chat_id=chat_id)
    bot.send_document(chat_id=chat_id, document=open("new_spacex/spacex_0.jpeg", 'rb'))

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sleep', help='sleep time',
        type=int,
        default=14400)
    args = parser.parse_args()
    while True:
        directory = "new_spacex/"
        filesindir = os.listdir(directory)
        list_telegram_pictures = []
        for filesindirs in filesindir:
            path = os.path.join(filesindirs)
            file = os.path.join(str(directory), path)
            list_telegram_pictures.append(file)
            time.sleep(args.sleep)
            bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
        return (list_telegram_pictures)

        for file in random.shuffle(list_telegram_pictures):
            bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
            time.sleep(args.sleep)


if __name__ == '__main__':
    main()


