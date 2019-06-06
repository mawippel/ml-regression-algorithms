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
    c = np.dot(c_betas[0], x) + c_betas[1]
    plt.plot(c, 'red')

    # y = 𝛽0 + 𝛽1X + 𝛽2X²
    d_betas = np.polyfit(x, y, 2)
    d = np.add ( np.add( np.dot(np.power(x, 2), d_betas[0]), np.dot(x, d_betas[1]) ), d_betas[2] )
    plt.plot(d, 'green')

		# y = 𝛽0 + 𝛽1X + 𝛽2X² + 𝛽3X³
		d_betas = np.polyfit(x, y, 3)


		# y = 𝛽0 + 𝛽1X + 𝛽2X² + 𝛽3X³ + 𝛽2X4 + 𝛽3X5 + 𝛽2X6 + 𝛽3X7 + 𝛽3X8
		d_betas = np.polyfit(x, y, 8)

    plt.show()


    e_betas = np.polyfit(x, y, 3)
    f_betas = np.polyfit(x, y, 8)

    # print(d_betas)
    # print(e_betas)
    # print(f_betas)

    

if __name__ == "__main__":
    main()