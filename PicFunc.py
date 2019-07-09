from PIL import Image
import numpy as np


def parseImage(path_to_image):
    original = Image.open(path_to_image)

    return original


def getListofPixels(original):
    pixels_list = []
    width, height = original.size

    for x in range(width):
        for y in range(height):
            pixels_list.append(original.getpixel((x, y)))

    return pixels_list


def applyLinearTrans(matrix, vector):
    return np.dot(matrix, vector)


def getChangedPixels(pixels_list, matrix):
    new_pixels_list = []

    for pixel in pixels_list:
        new_pixels_list.append(applyLinearTrans(matrix, pixel))

    return new_pixels_list


def getImageFromPixelsList(pixel_list, width, height):
    new_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            [r, g, b] = pixel_list[y + x*height]
            new_image.putpixel((x, y), (abs(int(r)), abs(int(g)), abs(int(b))))

    return new_image


def getChangedImage(path_to_image, matrix):
    original = parseImage(path_to_image)
    width, height = original.size
    pixels_list = getListofPixels(original)
    new_pixels_list = getChangedPixels(pixels_list, matrix)
    new_image = getImageFromPixelsList(new_pixels_list, width, height)

    return new_image
