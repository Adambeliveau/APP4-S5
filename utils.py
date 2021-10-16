import numpy as np
import matplotlib.pyplot as plt


def load_img(filename) -> np.ndarray:
    return np.load(filename)


def to_gray(filename):
    plt.gray()
    img_color = plt.imread(filename)
    return np.mean(img_color, -1)
