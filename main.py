from PicFunc import *
from VectorRotate import getRotatedImage
from ImageColors3D import get3DColorMap


config = {
    'img_path': 'mona_lisa.jpg'
}


if __name__ == "__main__":
    sym_matrix = np.array(
        [
            [0.0, 0.5, 0.5],
            [0.5, 0.0, 0.5],
            [0.5, 0.5, 0.0]
        ]
    )

    diagonal_matrix = np.array(
        [
            [1.5, 0, 0],
            [0, 0.5, 0],
            [0, 0, 2]
        ]
    )

    # new_image = getChangedImage(config['img_path'], sym_matrix)
    # new_image.save('new_mona_lisa5.jpg')

    # new_image = getChangedImage(config['img_path'], diagonal_matrix)
    # new_image.save('diagonal_mona_lisa.jpg')

    new_image = getRotatedImage(config['img_path'], x_rotate=-40, y_rotate=-40, z_rotate=15)
    new_image.save('new_mona_lisa.jpg')

    get3DColorMap(config['img_path']).show()
    get3DColorMap('new_mona_lisa.jpg').show()

