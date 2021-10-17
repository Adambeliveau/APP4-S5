import numpy as np
from scipy import signal


def transfer_fct(method: str):
    if method == 'bilineaire':
        print(method)
        b = np.array([0.418, 0.835, 0.418])
        a = np.array([1, 0.463, 0.209])
    elif method == 'butter':
        [b, a] = butter()
    elif method == 'cheby1':
        [b, a] = cheby1()
    elif method == 'cheby2':
        [b, a] = cheby2()
    elif method == 'ellip':
        [b, a] = ellip()
    else:
        b = np.array([])
        a = np.array([])
    return b, a


def filter_img(img, method: str):
    b, a = transfer_fct(method)

    return signal.lfilter(b, a, img)


def butter():
    n, W_n = signal.buttord(500, 750, 0.2, 60, fs=1600)
    print(n)
    return signal.butter(n, W_n, fs=1600)


def cheby1():
    n, W_n = signal.cheb1ord(500, 750, 0.2, 60, fs=1600)
    print(n)
    return signal.cheby1(n, 0.2, W_n, fs=1600)


def cheby2():
    n, W_n = signal.cheb2ord(500, 750, 0.2, 60, fs=1600)
    print(n)
    return signal.cheby2(n, 0.2, W_n, fs=1600)


def ellip():
    n, W_n = signal.ellipord(500, 750, 0.2, 60, fs=1600)
    print(n)
    return signal.ellip(n, 0.2, 60, W_n, fs=1600)
