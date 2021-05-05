import os
import requests
import urllib3


from pathlib import Path
from urllib.parse import urlsplit, unquote, urlunparse


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


import pprint


def fetch_spacex_launch(url, filepath):
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_image_links(url):
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr_images']
    return image_links


def get_file_extension(url):
    extension = os.path.splitext(urlsplit(url).path)[-1]
    return extension


def fetch_hubble_photo(url, image_id, filepath, extension):
    hubble_image_filepath = os.path.join(filepath, f'{image_id}{extension}')
    print(url)
    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(hubble_image_filepath, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    # spacex_url = 'https://api.spacexdata.com/v3/launches/108'
    # image_links = get_image_links(spacex_url)

    # for link_number, link in enumerate(image_links):
    #     filename = f'spacex{link_number + 1}.jpeg'
    #     filepath = os.path.join(folder, filename)

    #     fetch_spacex_launch(link, filepath)


    image_id = 1
    hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(hubble_url)
    response.raise_for_status()
    image_links = response.json()['image_files']
    hubble_image_links = [f'http:{link["file_url"]}' for link in response.json()['image_files']]

    # pprint.pprint(hubble_image_links)
    fetch_hubble_photo(hubble_image_links[-1], image_id, folder, get_file_extension(hubble_image_links[-1]))
    
