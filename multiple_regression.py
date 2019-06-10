import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data
import numpy as np
import correlation_regression
import matricesUtils


def main():
    # Populate these variables with the data that will be used
    data_matrix = data.getMatrix()
    matrix_x = matricesUtils.matrix_indX(data_matrix)
    matrix_x_without_one = matricesUtils.matrix_indX_without_one(data_matrix)
    matrix_y = matricesUtils.matrix_indY(data_matrix)
    house_sizes = matricesUtils.getHouseSizes(data_matrix)
    num_bedrooms = matricesUtils.getNumOfBedrooms(data_matrix)

    # Verifies the correlation and regression for 'House Size' and 'Price', using the correlation_regression.py script
    r1 = correlation_regression.correlacao(house_sizes, matrix_y)
    b1 = correlation_regression.regressaoB1(house_sizes, matrix_y)
    b0 = correlation_regression.regressaoB0(house_sizes, matrix_y, b1)
    correlation_regression.montarGrafico(house_sizes, matrix_y, b0, b1, r1)

    # Verifies the correlation and regression for 'Number of bedrooms' and 'Price', using the correlation_regression.py script
    r1 = correlation_regression.correlacao(num_bedrooms, matrix_y)
    b1 = correlation_regression.regressaoB1(num_bedrooms, matrix_y)
    b0 = correlation_regression.regressaoB0(num_bedrooms, matrix_y, b1)
    correlation_regression.montarGrafico(num_bedrooms, matrix_y, b0, b1, r1)

    # Calculate the multiple linear regression
    beta = multiple_reg(matrix_x_without_one, matrix_y)
    newZ = regression_line(matrix_x, beta)

    # Plots the 3D graph
    plot_3d_graph(house_sizes, num_bedrooms, matrix_y, newZ)


def multiple_reg(x, y):
    """
        Executes the following equation, generating a beta:
            (Xt X)-1 Xt y
    """

    # Inserts 1 in the first column
    x = np.insert(x, 0, 1, axis=1)

    # Executes the equation
    transpose_x = np.transpose(x)
    transpose_x_times_x = np.dot(transpose_x, x)
    inverse_transpose_x_times_x = np.linalg.inv(transpose_x_times_x)
    transpose_x_times_y = np.dot(transpose_x, y)
    return np.dot(inverse_transpose_x_times_x, transpose_x_times_y)


def regression_line(x, beta):
    """
        Executes the equation
            𝑦̂ = X𝛽
    """
    print('House size (1650) | Bedrooms (3): R$ ', np.dot([1, 1650, 3], beta))
    return np.dot(x, beta)


def plot_3d_graph(x, y, z, newZ):
    """
        Build and plot the 3D Chart based on x, y and z. It's also plotted the new z, that represents the prices
        calculated by this algorithm
    """
    fig = plt.figure()
    ax = Axes3D(fig)

    # Scatter of: House Size | Number of Bedrooms | Real price (came from matrix)
    ax.scatter(x, y, z)
    # Plot of: House Size | Number of Bedrooms | calculated price
    plt.plot(x, y, newZ, 'r')
    plt.show()


if __name__ == "__main__":
    main()
