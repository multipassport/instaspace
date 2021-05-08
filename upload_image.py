import glob
import os
import logging

from dotenv import load_dotenv
from instabot import Bot
from PIL import Image
from urllib.parse import urlsplit


def thumbnail_image(photo, image_size):
    new_image_name = photo.replace(os.path.splitext(photo)[-1], '.jpg')
    image = Image.open(photo)
    image.thumbnail(image_size)
    image.convert('RGB').save(new_image_name, 'JPEG')
    return image


def get_file_extension(url):
    extension = os.path.splitext(urlsplit(url).path)[-1]
    return extension


if __name__ == '__main__':
    load_dotenv()
    logging.basicConfig(filename="upload_image.log", filemode='w')

    folder_path = "./images"
    image_maximal_size = (1080, 1080)
    images = [image for image in glob.glob(folder_path + '/*.jpg')]

    for image in os.listdir('./images'):
        thumbnail_image(f'./images/{image}', image_maximal_size)

    bot = Bot()
    bot.login(
        username=os.getenv('INSTAGRAM_USERNAME'),
        password=os.getenv('INSTAGRAM_PASSWORD'),
        )

    for image in images:
        try:
            print(f'Uploading {image}')
            bot.upload_photo(image)
        except Exception as error:
            print(str(error))
            logging.error(error)
