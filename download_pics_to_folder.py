# Download pictures to folder

import requests
def download_pics(my_path, url, file_name):
    filename =(f'{my_path}/{file_name}.jpeg')
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

#download_pics('images/', 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'hubble2')
