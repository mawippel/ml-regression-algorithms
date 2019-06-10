"""
    Qual dos datasets não é apropriado para regressão linear?
    R: O ultimo grafico, ja que, o eixo y varia sem existir uma variacao no eixo x.
"""

import copy
import math
import matplotlib.pyplot as plt

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]


def main():
    # runs the correlation method for the 3 datasets
    r1 = correlacao(x1, y1)
    r2 = correlacao(x2, y2)
    r3 = correlacao(x3, y3)

    # runs the beta 1 method for the 3 datasets
    b11 = regressaoB1(x1, y1)
    b12 = regressaoB1(x2, y2)
    b13 = regressaoB1(x3, y3)

    # runs the beta 0 method for the 3 datasets
    b01 = regressaoB0(x1, y1, b11)
    b02 = regressaoB0(x2, y2, b12)
    b03 = regressaoB0(x3, y3, b13)

    # plot the 3 graphs 
    montarGrafico(x1, y1, b01, b11, r1)
    montarGrafico(x2, y2, b02, b12, r2)
    montarGrafico(x3, y3, b03, b13, r3)


def correlacao(x, y):
    """
        Executes the following equation:
            Σ(x−x̄)(y−ȳ) / √(Σ(x−x̄)² Σ(y−ȳ)²)
    """
    xAvg = average(x)
    yAvg = average(y)
    divisor = 0
    dividendoX = 0
    dividendoY = 0

    for i in range(0, len(x)):
        divisor += (x[i] - xAvg) * (y[i] - yAvg)

        dividendoX += (x[i] - xAvg) ** 2
        dividendoY += (y[i] - yAvg) ** 2

    dividendo = dividendoX * dividendoY
    dividendo = math.sqrt(dividendo)

    return divisor / dividendo


def regressaoB1(x, y):
    """
        Executes the following equation, to get the beta 1 value:
            Σ(x−x̄)(y−ȳ) /	Σ(x−x̄)²
    """
    xAvg = average(x)
    yAvg = average(y)
    divisor = 0
    dividendo = 0

    for i in range(0, len(x)):
        divisor += (x[i] - xAvg) * (y[i] - yAvg)
        dividendo += (x[i] - xAvg) ** 2

    return divisor / dividendo

def regressaoB0(x, y, b1):
    """
        Executes the following equation, to get the beta 0 value:
            𝑦̄− β1𝑥̄
    """
    xAvg = average(x)
    yAvg = average(y)
    return yAvg - (b1 * xAvg)

def calcularCoeficienteCorrelacao(b0, b1, x):
    """
        Executes the following equation, to get the regression line:
            𝛽0+𝛽1x
    """
    y = []
    for i in range(0, len(x)):
        y.append(b0 + (b1*x[i]))
    return y


def average(lst):
    """
        Get the average value of an array
    """
    return sum(lst) / len(lst)


def montarGrafico(x, y, b0, b1, r):
    """
        Build and plot the graph based on x, y and the correlation coeficient
    """
    plt.scatter(x, y)
    plt.plot(x, calcularCoeficienteCorrelacao(b0, b1, x), 'r')
    plt.title('r=' + str(round(r, 4)) + ' b0=' + str(round(b0, 4)) + ' b1=' + str(round(b1, 4)))
    plt.show()


if __name__ == "__main__":
    main()
