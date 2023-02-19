# Downloads photos from Spasex and NASA (APOD and EPIC) to your computer and post in Telegram Channel

## How to install
Python has to be installed.
Clon the repository.
Install the dependencies:

`pip install -r requiremnts.txt`

Get your API key at https://api.nasa.gov/ and save in Notepad as NASA_KEY in file.env in the same directory.
Create a bot and get your token from BotFather in Telegram and save it as TELEGRAM_BOT_TOKEN in file .env.


`NASA_KEY=c5c5f7977f14e54af...`
`TELEGRAM_BOT_TOKEN = 34erT664...`

Make your bot an administrator of a channel.  
Create folder 'nasa' in your directory

## Description of the program

Run the program by typing in the Terminal: 

`python download_photos_from_nasa.py`

![code on command line](/2023-02-16.png)

The program will first download the EPIC photos from NASA page, save them in directory /nasa 
and then post them in your channel one by one every 4 hours, unless you specify other time by inputing the number of seconds 
after python download_photos_from_nasa.py. When all pictures are posted, it will post them again, reshuffled.


## download_photos_from_nasa()

Save images available from the NASA epic site in a separate files, grouped in a folder.

Images posted in a Telegram Channel 

## Functions in the package

## `fetch_spacex(path, launch_id)`

The fuction will download a list of Spacex launch pictures for a given launch ID. If no ID is provided, the latest ID will be used.


## `fetch_apod(path)`

The fuction will download a NASA picture of the day.


## `download_epic_pics()`

This function creates a list of images from a site:  

`https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY`

Saves them in a list 'epic_images'


### Algorithm:

1. Create a list 'epic_images'
2. Using the names of images, add .png extensions.
3. Create a list urls, where the name of the png file is a part of url.
4. Create folder nasa/ in your computer.
5. Save each image in a separate file in a 'nasa/' folder.


