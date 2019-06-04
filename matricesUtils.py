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


def getHouseSizes(m):
    houses = []
    for i in range(0, len(m)):
        houses.append(m[i][0])
    return houses


def getNumOfBedrooms(m):
    bedrooms = []
    for i in range(0, len(m)):
        bedrooms.append(m[i][1])
    return bedrooms