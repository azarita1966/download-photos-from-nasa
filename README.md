# download-photos-from-nasa

## Downloads photos from NASA EPIC to your computer

###download_epic_pics()



Creates a list of images, available from the NASA epic site: 

`https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY`


Saves them in a list 'epic_images'


###Algorithm:

1. Create a list 'epic_images'.
2. Save current date and time in a varaible 'now'.
3. Using the names of images, add .png extensions.
4. Create a list urls, where the name of the png file is a part of url.
5. Create folder nasa/ in your computer.
6. Save each image in a separate file in a nasa/ folder.
