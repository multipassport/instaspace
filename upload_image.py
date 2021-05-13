import glob
import os
import logging

from dotenv import load_dotenv
from fetch_photo import get_file_extension
from instabot import Bot
from PIL import Image
from requests.exceptions import ConnectionError
from urllib.parse import urlsplit


def thumbnail_image(photo, image_size):
    new_image_name = photo.replace(os.path.splitext(photo)[-1], '.jpg')
    image = Image.open(photo)
    image.thumbnail(image_size)
    image.convert('RGB').save(new_image_name, 'JPEG')
    return image


if __name__ == '__main__':
    load_dotenv()
    logging.basicConfig(filename='upload_image.log', filemode='w')

    folder_path = './images'
    image_maximal_size = (1080, 1080)

    for image in os.listdir(folder_path):
        thumbnail_image(os.path.join(folder_path, image), image_maximal_size)

    images = glob.glob(f'{folder_path}/*.jpg')

    bot = Bot()
    bot.login(
        username=os.getenv('INSTAGRAM_USERNAME'),
        password=os.getenv('INSTAGRAM_PASSWORD'),
        )

    for image in images:
        try:
            bot.upload_photo(image)
        except ConnectionError as error:
            logging.error(error)
