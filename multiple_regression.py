import math
import matplotlib.pyplot as plt
import data


def main():
    m = data.getMatrix()
    mx = matrix_indX(m)
    my = matrix_indY(m)
    mtx = transpose_matrix(mx)
    multiply_matrix(mtx, mx)


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


def multiply_matrix(m1, m2):
    result = [[0 for x in range(len(m1))] for y in range(len(m2))]
    for i in range(len(m1)):
        # iterating by coloum by m2
        for j in range(len(m2[0])):
            # iterating by rows of m2
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    for r in result:
        print(r)


if __name__ == "__main__":
    main()
