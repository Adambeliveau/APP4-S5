import matplotlib.pyplot as plt
import numpy as np

from aberration import remove_aberration
from filtering import filter_img
from rotation import rotate
from utils import load_img, to_gray
from zplane import zplane

if __name__ == '__main__':
    img_aberration = load_img('Ressources/image_complete.npy')
    img_without_aberration = remove_aberration(img_aberration)
    plt.imsave('Ressources/img_without_aberrations.png', img_without_aberration)
    img_gray = to_gray('Ressources/img_without_aberrations.png')
    plt.imsave('Ressources/img_without_aberrations_gray.png', img_gray)
    img_rotated = rotate(img_without_aberration)
    plt.imsave('Ressources/img_rotated.png', img_rotated)
    img_filtered_bilineaire = filter_img(img_rotated, 'bilineaire')
    img_filtered_butter = filter_img(img_rotated, 'butter')
    img_filtered_cheby1 = filter_img(img_rotated, 'cheby1')
    img_filtered_cheby2 = filter_img(img_rotated, 'cheby2')
    img_filtered_ellip = filter_img(img_rotated, 'ellip')
    plt.imsave('Ressources/img_filtered_bilineaire.png', img_filtered_bilineaire)
    plt.imsave('Ressources/img_filtered_butter.png', img_filtered_butter)
    plt.imsave('Ressources/img_filtered_cheby1.png', img_filtered_cheby1)
    plt.imsave('Ressources/img_filtered_cheby2.png', img_filtered_cheby2)
    plt.imsave('Ressources/img_filtered_ellip.png', img_filtered_ellip)





