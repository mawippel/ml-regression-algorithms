import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data
import numpy as np
import correlation_regression
import matricesUtils


def main():
    m = data.getMatrix()
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
    mtx = matricesUtils.transpose_matrix(mx)
    result = multiply_matrix(mtx, mx, my)
    regression_line(mx, result)
    plot_3d_graph(tamanhoCasas, numQuartos, my)


# Executes the equation: 𝛽 = (Xt X)-1 Xt y
def multiply_matrix(transposeMatrix, xMatrix, pricesArray):
    aux = np.matrix(transposeMatrix) * np.matrix(xMatrix)
    firstMultiplication = aux.tolist()

    # Elevação de todos os valores da matriz por -1
    for i in range(len(firstMultiplication)):
        for j in range(len(firstMultiplication)):
            firstMultiplication[i][j] = firstMultiplication[i][j] ** -1

    # Multiplicar essa matriz pela matriz transposta
    multipliedMatrix = np.matrix(
        firstMultiplication) * np.matrix(transposeMatrix)

    # Multiplicar a matriz por y (preço)
    # print(np.array(multipliedMatrix).dot(np.array(pricesArray)))
    result = np.array(multipliedMatrix).dot(np.array(pricesArray))
    print(result.tolist())
    return result.tolist()


def regression_line(m2, result):
    # 𝑦̂ = X*𝛽
    teste = np.array(m2).dot(np.array(result))
    print(teste)


def plot_3d_graph(x, y, z):
    # Plotar o Gráfico de Dispersão 3D
    fig = plt.figure()
    ax = Axes3D(fig)

    # Scatter de Tamanho | numero de quartos | preco real (que veio da matriz)
    ax.scatter(x, y, z)
    plt.show()

    # Plot  de Tamanho | numero de quartos | preco calculado


if __name__ == "__main__":
    main()
