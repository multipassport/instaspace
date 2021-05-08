import os
import requests

from pathlib import Path
from requests.exceptions import ConnectionError


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


if __name__ == '__main__':
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    spacex_url = 'https://api.spacexdata.com/v3/launches/108'
    image_links = get_image_links(spacex_url)

    for link_number, link in enumerate(image_links):
        filename = f'spacex{link_number + 1}.jpg'
        filepath = os.path.join(folder, filename)

        fetch_spacex_launch(link, filepath)
