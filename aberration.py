import numpy as np
from scipy import signal


def get_fct_inverse():
    z1 = 0
    z2 = -0.99
    z3 = -0.99
    z4 = 0.8
    p1 = 0.9 * np.e ** ((1j * np.pi) / 2)
    p2 = 0.9 * np.e ** ((-1j * np.pi) / 2)
    p3 = 0.95 * np.e ** ((1j * np.pi) / 8)
    p4 = 0.95 * np.e ** ((-1j * np.pi) / 8)
    b = np.poly((z1, z2, z3, z4))
    a = np.poly((p1, p2, p3, p4))
    return b, a


def apply_fct_inverse(x_n):
    b, a = get_fct_inverse()
    return signal.lfilter(b, a, x_n)


def remove_aberration(gh_aberration):
    return [apply_fct_inverse(x_n) for x_n in gh_aberration]
