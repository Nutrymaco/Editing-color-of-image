from PicFunc import *
import numpy as np
import math


def convert_degrees_to_radian(degrees):
    return degrees*math.pi/180


def get_rotated_image(path_to_image, x_rotate=0, y_rotate=0, z_rotate=0):

    original = parse_image(path_to_image)
    width, height = original.size
    pixels_list = get_list_of_pixels(original)

    if x_rotate:  # red
        x_rotate_matrix = get_x_rotating_matrix(x_rotate)
        pixels_list = get_changed_pixels(pixels_list, x_rotate_matrix)

    if y_rotate:  # green
        y_rotate_matrix = get_y_rotation_matrix(y_rotate)
        pixels_list = get_changed_pixels(pixels_list, y_rotate_matrix)

    if z_rotate:  # blue
        z_rotate_matrix = get_z_rotation_matrix(z_rotate)
        pixels_list = get_changed_pixels(pixels_list, z_rotate_matrix)

    return get_image_from_pixels_list(pixels_list, width, height)


def get_x_rotating_matrix(degrees):
    radian = convert_degrees_to_radian(degrees)
    rotate_matrix = np.array(
        [
            [1, 0, 0],
            [0, np.cos(radian), -np.sin(radian)],
            [0, np.sin(radian), np.cos(radian)]
        ]
    )

    return rotate_matrix


def get_y_rotation_matrix(degrees):
    radian = convert_degrees_to_radian(degrees)
    rotate_matrix = np.array(
        [
            [np.cos(radian), 0, np.sin(radian)],
            [0, 1, 0],
            [-np.sin(radian), 0, np.cos(radian)]
        ]
    )

    return rotate_matrix


def get_z_rotation_matrix(degrees):
    radian = convert_degrees_to_radian(degrees)
    rotate_matrix = np.array(
        [
            [np.cos(radian), -np.sin(radian), 0],
            [np.sin(radian), np.cos(radian),0],
            [0, 0, 1]
        ]
    )

    return rotate_matrix
