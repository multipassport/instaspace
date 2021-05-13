import os
import requests
import urllib3

from fetch_photo import fetch_photo
from pathlib import Path
from requests.exceptions import ConnectionError
from urllib.parse import urlsplit


def get_file_extension(url):
    extension = os.path.splitext(urlsplit(url).path)[-1]
    return extension


def fetch_hubble_collection_image_ids(collection_name):
    hubble_collection_url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(hubble_collection_url)
    response.raise_for_status()
    collection_image_ids = [image_detail['id'] for image_detail in response.json()]
    return collection_image_ids


def get_image_link(url):
    response = requests.get(url)
    response.raise_for_status()
    hubble_image_link = f'http:{response.json()["image_files"][-1]["file_url"]}'
    return hubble_image_link
            

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    hubble_collection = 'holiday_cards'
    collection_image_ids = fetch_hubble_collection_image_ids(hubble_collection)

    for image_id in collection_image_ids:
        try:
            hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'
            hubble_image_link = get_image_link(hubble_url)
            extension = get_file_extension(hubble_image_link)
            hubble_image_filepath = os.path.join(folder, f'{image_id}{extension}')
            fetch_photo(hubble_image_link, hubble_image_filepath)
        except ConnectionError:
            print('Connection Error')
