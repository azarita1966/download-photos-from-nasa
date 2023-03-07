import os
import argparse
import random
import time
import telegram

from telegram import Update
from telegram.ext import Updater
from dotenv import load_dotenv
from pathlib import Path
from os.path import isfile, join
from os import listdir



def pick_files(folder='new_spasex'):
    return [Path.cwd() / folder / filename for filename in listdir(folder) if isfile(join(folder, filename))]


def send_telegram_photo(token, chat_id, image, sleep=5, caption=None):
    updater = Updater(token, use_context=True)
    dsp = updater.dispatcher
    with open(image, 'rb') as image_file:
        try:
            dsp.bot.send_photo(chat_id=chat_id, photo=image_file, caption=caption)
        except telegram.error.NetworkError:
            time.sleep(4)
            return False


def send_random_telegram_photo(token, chat_id, image, sleep=4):
    pictures = pick_files('new_spasex')
    random.shuffle(pictures)
    for image in pictures:
        send_telegram_photo(token, chat_id, image, caption=None)
        time.sleep(sleep*60*60)


def main(folder='new_spasex', sleep=4):
    token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()[0].message.chat
    chat_id = updates.id

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sleep', help='sleep time',
        type=int,
        default=4)
    parser.add_argument(
        '--folder', help='directory from where photos are posted',
        type=str,
        default="new_spasex")
    args = parser.parse_args()

    for image in pick_files(folder='new_spasex'):
        send_telegram_photo(token, chat_id, image, caption=None)
        time.sleep(sleep*60*60)
    send_random_telegram_photo(token, chat_id, image, sleep=4)

if __name__ == '__main__':
    load_dotenv()
    main(folder=args.folder, sleep=args.sleep)
