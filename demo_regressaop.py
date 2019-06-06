import scipy.io as scipy
import numpy as np

data = scipy.loadmat('data_preg.mat')['data']

def main():
    d_betas = np.polyfit(data[:,0], data[:,1], 2)
    e_betas = np.polyfit(data[:,0], data[:,1], 3)
    f_betas = np.polyfit(data[:,0], data[:,1], 8)

    print(d_betas)
    print(e_betas)
    print(f_betas)

    print(d_betas[2])

    x123 = np.array(np.dot(d_betas[0], data[:,0]), np.dot(d_betas[1], data[:,0])

    print(x123)

    print(np.sum(x123), axis=0))

if __name__ == "__main__":
    main()