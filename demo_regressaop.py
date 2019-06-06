import scipy.io as scipy
import numpy as np
import matplotlib.pyplot as plt

data = scipy.loadmat('data_preg.mat')['data']


def main():
    x = data[:, 0]
    y = data[:, 1]
    plt.scatter(x, y)

    # y = 𝛽0 + 𝛽1X
    c_betas = np.polyfit(x, y, 1)
    c = c_betas[1] + np.dot(c_betas[0], x)
    plt.plot(x, c, 'red')

    # y = 𝛽0 + 𝛽1X + 𝛽2X²
    d_betas = np.polyfit(x, y, 2)
    d = np.dot(np.power(x, 2), d_betas[0]) + np.dot(x, d_betas[1]) + d_betas[2]
    plt.plot(x, d, 'green')

    # y = 𝛽0 + 𝛽1X + 𝛽2X² + 𝛽3X³
    e_betas = np.polyfit(x, y, 3)
    e = np.dot(np.power(x, 3), e_betas[0]) + np.dot(np.power(x, 2),
                                                    e_betas[1]) + np.dot(x, e_betas[2]) + e_betas[3]
    plt.plot(x, e, 'black')

    # y = 𝛽0 + 𝛽1X + 𝛽2X² + 𝛽3X³ + 𝛽2X4 + 𝛽3X5 + 𝛽2X6 + 𝛽3X7 + 𝛽3X8
    f_betas = np.polyfit(x, y, 8)
    f = np.dot(np.power(x, 8), f_betas[0]) + np.dot(np.power(x, 7), f_betas[1]) + np.dot(np.power(x, 6), f_betas[2]) + np.dot(np.power(x, 5), f_betas[3]) + np.dot(np.power(x, 4), f_betas[4]) + np.dot(np.power(x, 3), f_betas[5]) + np.dot(np.power(x, 2),
                                                                                                                                                                                                                                             f_betas[6]) + np.dot(x, f_betas[7]) + f_betas[8]
    plt.plot(x, f, 'yellow')

    plt.show()


if __name__ == "__main__":
    main()
