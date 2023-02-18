# Downloads photos from Spasex and NASA (APOD and EPIC) to your computer

## How to install
Python has te be installed
Clon the repository
Install the dependencies:

`pip install -r requiremnts.txt`

Get your API key at https://api.nasa.gov/ and save in Notepad as NASA_KEY .env in the same directory

`NASA_KEY=c5c5f7977f14e54af...`

## Description of the program

Run the program by typing in the Terminal: 

`python download_photos_from_nasa.py`

![code on command line](/2023-02-16.png)


## download_photos_from_nasa()

Save images available from the NASA epic site in a separate files, grouped in a folder



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


