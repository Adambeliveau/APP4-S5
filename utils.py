import numpy as np
import matplotlib.pyplot as plt


def load_img(filename) -> np.ndarray:
    return np.load(filename)
