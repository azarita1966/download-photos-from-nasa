# Downloads photos from Spasex and NASA (APOD and EPIC) to your computer


## `download_pics(path, url, file_name)`

The function will downlad he picture from 'url' and save as 'file_name' in folder 'path'


## `fetch_spacex(path, launch_id)`

The fuction will download a list of Spacex launch pictures for a given launch ID. If no ID is provided, the latest ID will be used.


## `fetch_apod(path)`

The fuction will download a NASA picture of the day.


## `download_epic_pics()`

This function creates a list of images from a site:  

`https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY`

Saves them in a list 'epic_images'



## download_photos_from_nasa

Save images available from the NASA epic site in a separate files, grouped in a folder

### Algorithm:

1. Create a list 'epic_images'.

![alt text](C:\Users\44795\OneDrive\Pictures\Screenshots\2023-02-16.png)

2. Using the names of images, add .png extensions.
3. Create a list urls, where the name of the png file is a part of url.
4. Create folder nasa/ in your computer.
5. Save each image in a separate file in a 'nasa/' folder.
