def matrix_indX(m):
    mx = []
    for i in range(0, len(m)):
        mx.append([1, m[i][0], m[i][1]])
    return mx

def matrix_indX_without_one(m):
    mx = []
    for i in range(0, len(m)):
        mx.append([m[i][0], m[i][1]])
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