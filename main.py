import instabot
import os
import requests
import urllib3

from pathlib import Path
from PIL import Image
from requests.exceptions import ConnectionError
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
    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(hubble_image_filepath, 'wb') as file:
        file.write(response.content)


def thumbnail_image(photo, image_size):
    original_image = Image.open(photo)
    original_image.thumbnail(image_size)
    ready_to_publish_image = original_image.convert('CMYK')
    new_image_name = photo.replace(get_file_extension(photo), '.jpg')
    ready_to_publish_image.save(new_image_name, format='JPEG')
    return ready_to_publish_image


if __name__ == '__main__':
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    # spacex_url = 'https://api.spacexdata.com/v3/launches/108'
    # image_links = get_image_links(spacex_url)

    # for link_number, link in enumerate(image_links):
    #     filename = f'spacex{link_number + 1}.jpeg'
    #     filepath = os.path.join(folder, filename)

    #     fetch_spacex_launch(link, filepath)

    # hubble_collection = 'holiday_cards'
    # hubble_collection_url = f'http://hubblesite.org/api/v3/images/{hubble_collection}'
    # response = requests.get(hubble_collection_url)
    # response.raise_for_status()
    # collection_image_ids = [image_detail['id'] for image_detail in response.json()]

    # for image_id in collection_image_ids:
    #     try:
    #         hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    #         response = requests.get(hubble_url)
    #         response.raise_for_status()
    #     except ConnectionError:
    #         print('Error')
    #     else:
    #         hubble_image_link = f'http:{response.json()["image_files"][-1]["file_url"]}'
    #         print('downloading', image_id)

    #         fetch_hubble_photo(hubble_image_link, image_id, folder, get_file_extension(hubble_image_link))
    
    # image_size = (1200, 1200)
    # print(thumbnail_image('./images/4782.png', image_size))


    



