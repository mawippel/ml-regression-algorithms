"""
    k) Que método é o mais preciso neste caso?
    R: Para N=8, o EQM é sempre menor, ou seja, é mais preciso.
"""

import scipy.io as scipy
import numpy as np
import matplotlib.pyplot as plt
import random

# Load the matrix from the file
data = scipy.loadmat('data_preg.mat')['data']


def main():
    # load the x and y arrays into these variables, using list comprehension
    x = data[:, 0]
    y = data[:, 1]
    plt.scatter(x, y)

    # Calculate each regression line by doing a polyfit and solving the polynom
    n1 = calculateN1(x, y)
    n2 = calculateN2(x, y)
    n3 = calculateN3(x, y)
    n8 = calculateN8(x, y)

    # Plot the regression lines
    plt.show()
    plt.clf()

    # Calculate MSE (Mean Squared Error) for each regression that was calculated
    mse1 = calculateMSE(n1, y)
    mse2 = calculateMSE(n2, y)
    mse3 = calculateMSE(n3, y)
    mse8 = calculateMSE(n8, y)

    print(mse1)
    print(mse2)
    print(mse3)
    print(mse8)

    testData = []
    # Get the data left as the test data
    testData = random.choices(data, k=5)

    # Get 10% of the array as the training data
    a1_rows = set(map(tuple, data))
    a2_rows = set(map(tuple, testData))
    trainingData = a1_rows.difference(a2_rows)
    trainingData = sorted(trainingData, key=takeFirst)

    # Extract the trained data from the object
    trainedX = []
    trainedY = []
    for tmp1 in trainingData:
        trainedX.append(tmp1[0])
        trainedY.append(tmp1[1])

    # Extract the test data from the object
    testX = []
    testY = []
    for tmp3 in range(0, len(testData)):
        testX.append(testData[tmp3][0])
        testY.append(testData[tmp3][1])

    # Run the regression line again, but now, using the trained data
    plt.scatter(x, y)
    n1 = calculateN1(trainedX, trainedY)
    betaN1 = np.polyfit(trainedX, trainedY, 1)
    n2 = calculateN2(trainedX, trainedY)
    betaN2 = np.polyfit(trainedX, trainedY, 2)
    n3 = calculateN3(trainedX, trainedY)
    betaN3 = np.polyfit(trainedX, trainedY, 3)
    n8 = calculateN8(trainedX, trainedY)
    betaN4 = np.polyfit(trainedX, trainedY, 8)
    plt.show()
    plt.clf()

    # Calculates the regression using the betas from the trained data, but using the testData
    aux1 = betaN1[1] + np.dot(betaN1[0], testX)
    aux2 = np.dot(np.power(testX, 2), betaN2[0]) + np.dot(testX, betaN2[1]) + betaN2[2]
    aux3 = np.dot(np.power(testX, 3), betaN3[0]) + np.dot(np.power(testX, 2),
                                                    betaN3[1]) + np.dot(testX, betaN3[2]) + betaN3[3]
    aux8 = np.dot(np.power(testX, 8), betaN4[0]) + np.dot(np.power(testX, 7), betaN4[1]) + np.dot(np.power(testX, 6), betaN4[2]) + np.dot(np.power(testX, 5), betaN4[3]) + np.dot(np.power(testX, 4), betaN4[4]) + np.dot(np.power(testX, 3), betaN4[5]) + np.dot(np.power(testX, 2),
                                                                                                                                                                                                                                             betaN4[6]) + np.dot(testX, betaN4[7]) + betaN4[8]

    """
        Calculate the MSE using the regressions that were just calculated, to see the difference between the
        original MSE and the MSE calculated with the trained/test data
    """
    mse1 = calculateMSE(aux1, testY)
    mse2 = calculateMSE(aux2, testY)
    mse3 = calculateMSE(aux3, testY)
    mse8 = calculateMSE(aux8, testY)

    # We should see smaller MSE numbers here
    print ('-------------------')
    print(mse1)
    print(mse2)
    print(mse3)
    print(mse8)

def calculateMSE(regression_line, y):
    residual = 0
    for i in range(0, len(y)):
        residual += ((y[i] - regression_line[i])**2)
    return residual/len(y)


def takeFirst(elem):
    return elem[0]


def calculateN1(x, y):
    """
        y = 𝛽0 + 𝛽1X
    """
    c_betas = np.polyfit(x, y, 1)
    c = c_betas[1] + np.dot(c_betas[0], x)
    plt.plot(x, c, 'red')
    return c


def calculateN2(x, y):
    """
        y = 𝛽0 + 𝛽1X + 𝛽2X²
    """
    d_betas = np.polyfit(x, y, 2)
    d = np.dot(np.power(x, 2), d_betas[0]) + np.dot(x, d_betas[1]) + d_betas[2]
    plt.plot(x, d, 'green')
    return d


def calculateN3(x, y):
    """
        y = 𝛽0 + 𝛽1X + 𝛽2X² + 𝛽3X³
    """
    e_betas = np.polyfit(x, y, 3)
    e = np.dot(np.power(x, 3), e_betas[0]) + np.dot(np.power(x, 2),
                                                    e_betas[1]) + np.dot(x, e_betas[2]) + e_betas[3]
    plt.plot(x, e, 'black')
    return e


def calculateN8(x, y):
    """
        y = 𝛽0 + 𝛽1X + 𝛽2X² + 𝛽3X³ + 𝛽2X4 + 𝛽3X5 + 𝛽2X6 + 𝛽3X7 + 𝛽3X8
    """
    f_betas = np.polyfit(x, y, 8)
    f = np.dot(np.power(x, 8), f_betas[0]) + np.dot(np.power(x, 7), f_betas[1]) + np.dot(np.power(x, 6), f_betas[2]) + np.dot(np.power(x, 5), f_betas[3]) + np.dot(np.power(x, 4), f_betas[4]) + np.dot(np.power(x, 3), f_betas[5]) + np.dot(np.power(x, 2),
                                                                                                                                                                                                                                             f_betas[6]) + np.dot(x, f_betas[7]) + f_betas[8]
    plt.plot(x, f, 'yellow')
    return f

if __name__ == "__main__":
    main()
