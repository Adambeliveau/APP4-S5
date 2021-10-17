import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

wp = 500
ws = 750
gpass = 0.2
gstop = 60
fs = 1600

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
    w, h = signal.freqz(b, a)
    plt.figure()
    plt.plot(w, 20 * np.log10(np.abs(h)))
    plt.title(f'{method} filter')
    plt.ylabel('amplitude (dB)')
    plt.xlabel('w (éch/rad)')
    plt.axvline((2 * np.pi * ws)/fs, color='r')
    plt.axvline((2 * np.pi * wp)/fs, color='g')
    plt.axhline(-gpass, color='g')
    plt.axhline(-gstop, color='r')
    plt.savefig(f'Ressources/{method}_filter.png')

    return signal.lfilter(b, a, img)


def butter():
    n, W_n = signal.buttord(wp, ws, gpass, gstop, fs=fs)
    print(n)
    return signal.butter(n, W_n, fs=fs)


def cheby1():
    n, W_n = signal.cheb1ord(wp, ws, gpass, gstop, fs=fs)
    print(n)
    return signal.cheby1(n, gpass, W_n, fs=1600)


def cheby2():
    n, W_n = signal.cheb2ord(wp, ws, gpass, gstop, fs=fs)
    print(n)
    return signal.cheby2(n, gstop, W_n, fs=fs)


def ellip():
    n, W_n = signal.ellipord(wp, ws, gpass, gstop, fs=fs)
    print(n)
    return signal.ellip(n, gpass, gstop, W_n, fs=fs)
