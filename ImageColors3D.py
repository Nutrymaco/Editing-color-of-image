from PIL import Image
import numpy as np
from matplotlib import colors, pyplot as plt
from PicFunc import getListofPixels, parseImage
from mpl_toolkits.mplot3d import Axes3D
Axes3D = Axes3D


def getPlt(pixels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(0, 255)
    ax.set_ylim(255, 0)
    ax.set_zlim(0, 255)

    ax.set_xlabel('green (y)')
    ax.set_ylabel('red (x)')
    ax.set_zlabel('blue (b)')

    for r, g, b in pixels:
        ax.scatter(g, r, b, c=[[r / 255, g / 255, b / 255]])

    return plt


def get3DColorMap(path_to_image, percent=0.01):
    original = parseImage(path_to_image)
    pixels_list = np.unique(np.array(getListofPixels(original)), axis=0)

    pixels_list = pixels_list[::int(1/percent)]

    plt = getPlt(pixels_list)

    return plt
