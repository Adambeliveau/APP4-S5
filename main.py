import matplotlib.pyplot as plt

from utils import load_img
from aberration import remove_aberration
from zplane import zplane

if __name__ == '__main__':
    gh_aberration = load_img('Ressources/goldhill_aberrations.npy')
    print(gh_aberration[0])
    plt.figure()
    plt.imshow(gh_aberration)
    y_n = remove_aberration(gh_aberration)
    plt.figure()
    plt.imshow(y_n)
    plt.show()



