import os
from PIL import Image

INPUT_DIR = '/Volumes/SD/deeplearning/data/mosaic/input/'
INPUT_CROPPED_DIR = '/Volumes/SD/deeplearning/data/mosaic/input_cropped/'
OUTPUT_DIR = '/Volumes/SD/deeplearning/data/mosaic/input_resized/'

# def crop(image, size):
#     width, height = image.size
#
#     left = (width-size)/2
#     top = (height-size)/2
#     right = (width+size)/2
#     bottom = (height+size)/2
#
#     return image.crop((left, top, right, bottom))

for name in os.listdir(INPUT_DIR):
    if name == '.DS_Store':
        continue

    image = Image.open(INPUT_DIR + name)
    # image = crop(image)

    # image.save(INPUT_CROPPED_DIR, "JPEG", quality=100)

    image = image.resize((320, 320))
    image.save(OUTPUT_DIR + name, "JPEG", quality=100)