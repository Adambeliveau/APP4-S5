import numpy as np


class Compression:
    def __init__(self, img_filtered):
        self.img_filtered = img_filtered
        mat_cov = np.cov(img_filtered)
        _, self.eigenvectors = np.linalg.eig(mat_cov)

    def compression(self):
        img_v = np.matmul(self.eigenvectors.T, self.img_filtered)
        img_v[3*int(len(img_v)/10):] = 0
        return img_v

    def decompression(self, img_compressed):
        return np.matmul(np.linalg.inv(self.eigenvectors.T), img_compressed)



