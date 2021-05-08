import os
import requests
import urllib3

from pathlib import Path
from requests.exceptions import ConnectionError
from urllib.parse import urlsplit

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_file_extension(url):
    extension = os.path.splitext(urlsplit(url).path)[-1]
    return extension


def fetch_hubble_photo(url, image_id, filepath, extension):
    hubble_image_filepath = os.path.join(filepath, f'{image_id}{extension}')
    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(hubble_image_filepath, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    hubble_collection = 'wallpaper'
    hubble_collection_url = f'http://hubblesite.org/api/v3/images/{hubble_collection}'

    response = requests.get(hubble_collection_url)
    response.raise_for_status()
    collection_image_ids = [image_detail['id'] for image_detail in response.json()]

    for image_id in collection_image_ids:
        try:
            hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'
            response = requests.get(hubble_url)
            response.raise_for_status()
        except ConnectionError:
            print('Connection Error')
        else:
            hubble_image_link = f'http:{response.json()["image_files"][-1]["file_url"]}'
            extension = get_file_extension(hubble_image_link)

            print('downloading', image_id)
            fetch_hubble_photo(hubble_image_link, image_id, folder, extension)
