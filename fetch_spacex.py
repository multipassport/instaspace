import os
import requests

from fetch_photo import fetch_photo
from pathlib import Path
from requests.exceptions import ConnectionError


def get_image_links(url):
    response = requests.get(url)
    response.raise_for_status()

    image_links = response.json()['links']['flickr_images']
    return image_links


if __name__ == '__main__':
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    spacex_url = 'https://api.spacexdata.com/v3/launches/108'
    image_links = get_image_links(spacex_url)

    for link_number, link in enumerate(image_links, 1):
        filename = f'spacex{link_number}.jpg'
        filepath = os.path.join(folder, filename)
        try:
            fetch_photo(link, filepath)
        except ConnectionError:
            print('Connection Error')
