import numpy as np


def rotate(gh_without_aberration: np.ndarray):
    rotation_mat = np.array([[0, 1], [-1, 0]])
    rotated_img = np.zeros(gh_without_aberration.shape)
    for coords, val in np.ndenumerate(gh_without_aberration):
        i, j = np.matmul(rotation_mat, coords)
        rotated_img[i, j] = val

    return rotated_img

