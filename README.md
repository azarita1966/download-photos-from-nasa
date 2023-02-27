# Downloads photos from Spasex and NASA (APOD and EPIC) to your computer and post in Telegram Channel

## How to install
Python has to be installed.
Clon the repository.
Install the dependencies:

`pip install -r requirements.txt`

Get your API key at https://api.nasa.gov/ and 
save in Notepad as NASA_KEY in file .env in the same directory.
Create a bot and get your token from BotFather in Telegram and save 
hit as TELEGRAM_BOT_TOKEN in .env. 
Make your bot an administrator of a channel.


`NASA_KEY=c5c5f7977f14e54af...`

`TELEGRAM_BOT_TOKEN = 34erT664...`


## Description of the program download_photos_from_nasa()

Run the program by typing in the Terminal: 

`python download_photos_from_nasa.py`

![code on command line](/2023-02-16.png)

The program will first download the EPIC photos from NASA page, save them in directory /nasa 

### Algorithm:

1. Create a list 'epic_images'
2. Using the names of images, add .png extensions.
3. Create a list urls, where the name of the png file is a part of url.
4. Create folder nasa/ in your computer.
5. Save each image in a separate file in a 'nasa/' folder.


## Description of program telegram_bot.py

The program will post photos in your channel one by one every 4 hours, unless you specify other time by inputing the number of seconds 
after python download_photos_from_nasa.py. When all pictures are posted, it will post them again, reshuffled.

Run the program by typing in the Terminal: 

`python telegram_bot.py`

Images posted in a Telegram Channel:

![View in your telegram channel](/2023-02-271.png)


## Description of program fetch_spacex(path, launch_id):

Run the program by typing in the Terminal: 

`python fetch_spacex.py`

The fuction will download a list of Spacex launch pictures for a given launch ID. If no ID is provided, the latest ID will be used.

## Description of program fetch_apod(path):

Run the program by typing in the Terminal: 

`python fetch_apod.py`

The fuction will download a NASA picture of the day (APOD).


## Description of program download_pics_to_folder(path, url, file_name):

Run the program by typing in the Terminal: 

`python download_pics_to_folder.py`

This function downloads an image from a given url
Saves them in a given directory under given file name.



