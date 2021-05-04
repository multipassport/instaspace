import os
import requests

from pathlib import Path

import pprint


def fetch_spacex_last_launch(url, filepath):
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)
    return None


def get_image_links(url):
    response = requests.get(url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr_images']
    return image_links





if __name__ == '__main__':
    folder = './images'
    Path(folder).mkdir(exist_ok=True)

    # spacex_url = 'https://api.spacexdata.com/v3/launches/108'
    # image_links = get_image_links(spacex_url)

    # for link_number, link in enumerate(image_links):
    #     filename = f'spacex{link_number + 1}.jpeg'
    #     filepath = os.path.join(folder, filename)

    #     fetch_spacex_last_launch(link, filepath)
    image_id = 1
    hubble_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(hubble_url)
    response.raise_for_status()
    image_links = response.json()['image_files']
    for link in image_links:
        image_link = link['file_url']
