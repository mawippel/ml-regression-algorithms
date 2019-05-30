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
    r1 = generateRegression(x1, y1)
    r2 = generateRegression(x2, y2)
    r3 = generateRegression(x3, y3)

    # round(r1, 4)
    # round(r2, 4)
    # round(r3, 4)

    print(r1, r2, r3)

    b11 = calculateB1(x2, y1)
    b12 = calculateB1(x2, y2)
    b13 = calculateB1(x3, y3)

    # round(b11, 4)
    # round(b12, 4)
    # round(b13, 4)

    print(b11, b12, b13)

    b01 = calculateB0(x2, y1, b11)
    b02 = calculateB0(x2, y2, b12)
    b03 = calculateB0(x3, y3, b13)

    # round(b01, 4)
    # round(b02, 4)
    # round(b03, 4)

    print(b01, b02, b03)


def generateRegression(x, y):
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


def calculateB1(x, y):
    xAvg = average(x)
    yAvg = average(y)
    divisor = 0
    dividendo = 0

    for i in range(0, len(x)):
        divisor += (x[i] - xAvg) * (y[i] - yAvg)
        dividendo += (x[i] - xAvg) ** 2

    return divisor / dividendo


def calculateB0(x, y, b1):
    xAvg = average(x)
    yAvg = average(y)
    return yAvg - (b1 * xAvg)


def average(lst):
    return sum(lst) / len(lst)


if __name__ == "__main__":
    main()
