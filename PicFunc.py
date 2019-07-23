from PIL import Image
import numpy as np


def parse_image(path_to_image):
    original = Image.open(path_to_image)

    return original


def get_list_of_pixels(original):
    pixels_list = []
    width, height = original.size

    for x in range(width):
        for y in range(height):
            pixels_list.append(original.getpixel((x, y)))

    return pixels_list


def apply_linear_trans(matrix, vector):
    return np.dot(matrix, vector)


def get_changed_pixels(pixels_list, matrix):
    new_pixels_list = []

    for pixel in pixels_list:
        new_pixels_list.append(apply_linear_trans(matrix, pixel))

    return new_pixels_list


def get_image_from_pixels_list(pixel_list, width, height):
    new_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            [r, g, b] = pixel_list[y + x*height]
            new_image.putpixel((x, y), (abs(int(r)), abs(int(g)), abs(int(b))))

    return new_image


def get_changed_image(path_to_image, matrix):
    original = parse_image(path_to_image)
    width, height = original.size
    pixels_list = get_list_of_pixels(original)
    new_pixels_list = get_changed_pixels(pixels_list, matrix)
    new_image = get_image_from_pixels_list(new_pixels_list, width, height)

    return new_image
