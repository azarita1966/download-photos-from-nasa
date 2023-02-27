import telegram
import os
import argparse
import time
import dotenv

bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
updates = bot.get_updates()
chat_id = updates[-1].message.chat_id

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sleep', help='sleep time',
        type=int,
        default=14400)
    parser.add_argument(
        'directory', help='directory from where photos are posted',
        type=str,
        default="new_spacex/")
    args = parser.parse_args()

    while True:
        directory = args.directory
        pics_in_dirs = os.listdir(directory)
        telegram_pictures = []
        number_downloaded_pics = 0
        while number_downloaded_pics < len(pics_in_dirs):
            for nasa_pic in pics_in_dirs:
                path = os.path.join(nasa_pic)
                file = os.path.join(str(directory), path)
                telegram_pictures.append(file)
                time.sleep(args.sleep)
                with open(file, 'rb') as g:
                    document = g.read()
                bot.send_document(chat_id=chat_id, document=document)
                number_downloaded_pics += 1
            return telegram_pictures
        for file in random.shuffle(telegram_pictures):
            with open(file, 'rb') as g:
                document = g.read()
            bot.send_document(chat_id=chat_id, document=document)
            time.sleep(args.sleep)


if __name__ == '__main__':
    dotenv.load_dotenv()
    main()
