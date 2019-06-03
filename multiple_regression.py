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
    result = regmultipla(matricesUtils.matrix_indX_without_one(m), my)
    newZ = regression_line(np.array(mx), result)

    # Scatter de Tamanho | numero de quartos | preco real (que veio da matriz)
    # Plot de Tamanho | numero de quartos | preco calculado
    plot_3d_graph(tamanhoCasas, numQuartos, my, newZ)


# Executa a equação: 𝛽 = (Xt X)-1 Xt y
def regmultipla(x, y):
    # Insere 1 na primeira coluna
    x = np.insert(x, 0, 1, axis=1)

    # Transpõe a matriz X
    x_transposto = np.transpose(x)

    # (Xt X)
    x_transposto_vezes_x = np.dot(x_transposto, x)

    # (Xt X)-1
    x_transposto_vezes_x_inverso = np.linalg.inv(x_transposto_vezes_x)

    # Xt y
    x_transposto_vezes_y = np.dot(x_transposto, y)

    # (Xt X)-1 Xt y
    print(np.dot(x_transposto_vezes_x_inverso, x_transposto_vezes_y).tolist())
    return np.dot(x_transposto_vezes_x_inverso, x_transposto_vezes_y)


# Executa a equação: 𝑦̂ = X𝛽
def regression_line(x, beta):
    return np.dot(x, beta)


def plot_3d_graph(x, y, z, newZ):
    # Plotar o Gráfico de Dispersão 3D
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(x, y, z)
    plt.plot(x, y, newZ, 'r')
    plt.show()


if __name__ == "__main__":
    main()
