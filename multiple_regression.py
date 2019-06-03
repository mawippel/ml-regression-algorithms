import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data
import numpy as np
import correlation_regression
import matricesUtils


def main():
    m = data.getMatrix()
    mxWithoutOne = matricesUtils.matrix_indX_without_one(m)
    mx = matricesUtils.matrix_indX(m)
    my = matricesUtils.matrix_indY(m)

    tamanhoCasas = matricesUtils.getTamanhoCasas(m)
    numQuartos = matricesUtils.getNumQuartos(m)

    # Verifique a correlação e a regressão para Tamanho da casa e Preço
    r1 = correlation_regression.correlacao(tamanhoCasas, my)
    b1 = correlation_regression.regressaoB1(tamanhoCasas, my)
    b0 = correlation_regression.regressaoB0(tamanhoCasas, my, b1)
    correlation_regression.montarGrafico(tamanhoCasas, my, b0, b1, r1)

    # Número de quartos e Preço
    r1 = correlation_regression.correlacao(numQuartos, my)
    b1 = correlation_regression.regressaoB1(numQuartos, my)
    b0 = correlation_regression.regressaoB0(numQuartos, my, b1)
    correlation_regression.montarGrafico(numQuartos, my, b0, b1, r1)

    # Multiple Linear Regression
    result = multiply_matrix(mxWithoutOne, my)
    newY = regression_line(mx, result)

    # Scatter de Tamanho | numero de quartos | preco real (que veio da matriz)
    plot_3d_graph(tamanhoCasas, numQuartos, my, newY)

    # Plot  de Tamanho | numero de quartos | preco calculado
    # plot_3d_graph(tamanhoCasas, numQuartos, newY)


# Executes the equation: 𝛽 = (Xt X)-1 Xt y
def multiply_matrix(xMatrix, pricesArray):
    x = np.insert(xMatrix, 0, 1, axis=1)
    x_t = np.transpose(x)
    xt_x = np.dot(x_t, x)
    inverse_xt_x = np.linalg.inv(xt_x)
    xt_y = np.dot(x_t, pricesArray)
    result = np.dot(inverse_xt_x, xt_y)
    print(result)
    return result


def regression_line(x, result):
    # 𝑦̂ = X*𝛽
    print(np.dot(x, result))
    return np.dot(x, result)


def plot_3d_graph(x, y, z, newY):
    # Plotar o Gráfico de Dispersão 3D
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(x, y, z)
    plt.plot(x, newY, z, 'r')
    plt.show()


if __name__ == "__main__":
    main()
