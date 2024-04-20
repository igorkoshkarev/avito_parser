from PIL import Image
import os


def crop_image(image_path, location, size):
    image = Image.open(image_path)
    image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))\
         .save('cropped_image.png', 'PNG')
    del_image('avito_parser.png')


def del_image(image_name):
    os.remove(image_name)
