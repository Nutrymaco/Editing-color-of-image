from PicFunc import *
from VectorRotate import get_rotated_image
from ImageColors3D import get_3d_color_map


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
    original_image = parse_image(config['img_path'])
    original_image.show()

    new_image = get_changed_image(config['img_path'], sym_matrix)
    new_image.show()

    new_image = get_changed_image(config['img_path'], diagonal_matrix)
    new_image.show()

    new_image = get_rotated_image(config['img_path'], x_rotate=-40, y_rotate=-40, z_rotate=15)
    new_image.show()

    get_3d_color_map(config['img_path']).show()
    get_3d_color_map('new_mona_lisa.jpg').show()
