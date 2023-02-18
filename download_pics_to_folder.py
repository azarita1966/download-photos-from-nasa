import requests

def download_pics(path, url, file_name):
    filename =(f'{path}/{file_name}.jpeg')
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
