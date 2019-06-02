import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data
import numpy as np
import correlation_regression


def main():
    m = data.getMatrix()
    mx = matrix_indX(m)
    my = matrix_indY(m)

    tamanhoCasas = getTamanhoCasas(m)
    numQuartos = getNumQuartos(m)

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

    mtx = transpose_matrix(mx)
    multiply_matrix(mtx, mx, my, tamanhoCasas, numQuartos)


def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def matrix_indX(m):
    mx = []
    for i in range(0, len(m)):
        mx.append([1, m[i][0], m[i][1]])
    return mx


def matrix_indY(m):
    my = []
    for i in range(0, len(m)):
        my.append(m[i][2])
    return my


def getTamanhoCasas(m):
    casas = []
    for i in range(0, len(m)):
        casas.append(m[i][0])
    return casas


def getNumQuartos(m):
    quartos = []
    for i in range(0, len(m)):
        quartos.append(m[i][1])
    return quartos


def multiply_matrix(mt1, m2, m3y, tamanhoCasas, numQuartos):
    multipliedMatrix = np.matrix(mt1) * np.matrix(m2)
    mMultipliedMatrix = multipliedMatrix.tolist()

    # Elevação de todos os valores da matriz por -1
    for i in range(len(mMultipliedMatrix)):
        for j in range(len(mMultipliedMatrix)):
            mMultipliedMatrix[i][j] = mMultipliedMatrix[i][j] ** -1

    # Multiplicar essa matriz pela matriz transposta
    multipliedMatrix = np.matrix(mMultipliedMatrix) * np.matrix(mt1)

    # Multiplicar a matriz por y (preço)
    b1 = (np.array(multipliedMatrix[0]) * np.array(m3y)).tolist()
    b2 = (np.array(multipliedMatrix[1]) * np.array(m3y)).tolist()
    b3 = (np.array(multipliedMatrix[2]) * np.array(m3y)).tolist()

    # Final da equação 𝛽= (Xt X)-1 Xty
    result = []
    result.append(b1[0])
    result.append(b2[0])
    result.append(b3[0])

    # 𝑦̂ = X*𝛽
    teste = np.matrix(m2) * np.matrix(result)
    print(len(teste[0]))

    # Plotar o Gráfico de Dispersão 3D
    fig = plt.figure()
    ax = Axes3D(fig)

    # Scatter de Tamanho | numero de quartos | preco real (que veio da matriz)
    ax.scatter(tamanhoCasas, numQuartos, m3y)
    plt.show()

    # Plot  de Tamanho | numero de quartos | preco calculado
    
    





if __name__ == "__main__":
    main()
