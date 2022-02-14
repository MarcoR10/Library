import math
import NComplex as nc

# Adición de vectores complejos.
def svecto(a, b):
    num = len(a)
    suma = [(0, 0) for i in range(num)]
    for i in range(0, num):
        suma[i] = nc.sumacplx(a[i], b[i])
    return suma


# Inverso (aditivo) de un vector complejo
def invecto(a):
    num = len(a)
    inv = [(0, 0) for i in range(num)]
    for i in range(0, num):
        inv[i] = nc.conjucplx(a[i])
    return inv


# Multiplicación de un escalar por un vector complejo.
def multiexv(a, b):
    num = len(b)
    mult = [(0, 0) for i in range(num)]
    for i in range(0, num):
        mult[i] = nc.producplx(a, b[i])
    return mult


# Adición de matrices complejas
def sumatriz(a, b):
    num, num2 = len(a), len(a[0])
    resul = [[0 for i in range(num)] for j in range(num2)]
    for i in range(0, num):
        for j in range(0, num2):
            resul[i][j] = nc.sumacplx(a[i][j], b[i][j])
    return resul


# Inversa (aditiva) de una matriz compleja
def invematriz(a):
    num1 = len(a)
    num2 = len(a[0])
    invm = [[(0, 0) for i in range(num1)] for j in range(num2)]
    for i in range(0, num1):
        for j in range(0, num2):
            invm[i][j] = nc.conjucplx(a[i][j])
    return invm


# Multiplicación de un escalar por una matriz compleja.

def multriz(a, b):
    num, num2 = len(b), len(b[0])
    resul = [[0 for i in range(num)] for j in range(num2)]
    for i in range(0, num):
        for j in range(0, num2):
            resul[i][j] = nc.producplx(a, b[i][j])
    return resul


# Transpuesta de una matriz/vector
def tranmatriz(a):
    num = len(a)
    tran = [[(0, 0) for i in range(num)] for j in range(num)]
    for i in range(0, num):
        for j in range(0, len(a[i])):
            tran[i][j] = a[j][i]
    return tran


# Conjugada de una matriz/vector
def conjumatriz(a):
    num1 = len(a)
    num2 = len(a[0])
    conj = [[(0, 0) for i in range(num1)] for j in range(num2)]
    for i in range(0, num1):
        for j in range(0, num2):
            conj[i][j] = conjucplx2(a[i][j])
    return conj


# Adjunta (daga) de una matriz/vector
def dagamatriz(a):
    num1 = len(a)
    num2 = len(a[0])
    daga = [[(0, 0) for i in range(num1)] for j in range(num2)]
    for i in range(0, num1):
        for j in range(0, num2):
            daga[i][j] = conjucplx2(a[i][j])
            daga[i][j] = a[j][i]
    return daga


# Producto de dos matrices (de tamaños compatibles)
def proma(a, b):
    n, m = len(a), len(a[0])
    N, M = len(b), len(b[0])
    re = [[(0, 0) for j in range(m)] for i in range(n)]
    if m == N:
        for i in range(n):
            for j in range(M):
                for k in range(N):
                    p = nc.producplx(a[i][k], b[k][j])
                    q = re[i][j]
                    re[i][j] = nc.sumacplx(p, q)
    return re

# Función para calcular la "acción" de una matriz sobre un vector.
def accion(a,b):
    n, m = len(a), len(a[0])
    B = len(b)
    re = []
    if B == m:
        ceros = (0, 0)
        for i in range(n):
            for j in range(m):
                p = proma(a[i][j], b[j])
                ceros = nc.sumacplx(ceros, p)
            re += [ceros]
            ceros = (0, 0)
    return re

# Producto interno de dos vectores
def proint(a, b):
    num = len(b)
    mult = [0 for i in range(num)]
    real = 0
    img = 0
    for i in range(0, num):
        mult[i] = nc.producplx(a[i], b[i])
    for j in range(0,len(mult)):
        if mult[j][0] >= 0:
            real = real + int(mult[j][0])
        else:
            real = real + int(mult[j][0])*-1
        if mult[j][1] >= 0:
            img = img + int(mult[j][1])
        else:
            img = img + int(mult[j][1])*-1
    return real, img

# Norma de un vector
def norma(a):
    resul = 0
    for i in range(0, len(a)):
        raiz = (a[i][0] ** 2) + (a[i][1] ** 2)
        resul = resul + raiz
    resul = round(math.sqrt(resul), 2)
    return resul


# Distancia entre dos vectores
def dista(a,b):
    num = len(a)
    resta = [(0, 0) for i in range(num)]
    for i in range(0, num):
        resta[i] = nc.restacplx(a[i], b[i])
    resul = norma(resta)
    return resul

# Revisar si una matriz es unitaria
def uni(a):
    matr = proma(dagamatriz(a),a)
    ident = iden(len(a),len(a[0]))
    if matr == ident:
        return True
    else:
        return False

# Revisar si una matriz es hermitiana
def hermi(a):
    b = dagamatriz(a)
    if a == b:
        return True
    else:
        return False

#encuentra el producto tensor/cruz de dos matrices/vectores
def tensor(a,b):
    res = []
    m, n = 0, 0
    while (m<((len(a)-1)**2)):
        r1 = a[m]
        r2 = b[n]
        aux = []
        for i in r1:
            for j in r2:
                aux += [proma(i,j)]
        m += 1
        r2 = b[n]
        res += [aux]
        aux = []
        for i in r1:
            for j in r2:
                aux += [proma(i,j)]
        m += 1
        n -= 1
        res += [aux]
    return res
# -----------------------------------------------------------------------------------------------------------------------
def conjucplx2(a):
    real = a[0] * 1
    img = a[1] * -1
    return (real, img)
def iden(m,n):
    re = [[[0,0] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j:
                re[i][j] = ((2/2),0)
    return re
# -----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    # a = [(6.0,3.3),(4.9,5.8)]
    # a = [(2, 1), (3, 2), (1, 1)]
    #a = [(2, 1), (3, 2), (1, 1)]
    #b = [(5, 6), (4, 8), (16, 1)]
    #b = [(2,3),(4,3),(6,8)]
    #a = [[(2, 3), (0, 2), (1, 8)], [(3, 5), (0, 5), (0, 5)], [(5, 1), (1, 9), (1, 8)]]
    #b = [[(5, 7), (0, 8), (1, 2)], [(1, -5), (2, -5), (-4, -5)], [(1, 4), (1, -9), (0, 2)]]
    # print(svecto(a,b))
    # print(invecto(a))
    # print(multiexv((3, 2), [(6, 3), (0, 0), (5, 1), (4, 0)]))
    # print(sumatriz(a, b))
    # print(invematriz(a))
    # print(multriz(a, b))
    # print(tranmatriz(a))
    # print(conjumatriz(a))
    # print(dagamatriz(a))
    #print(proma(a, b))
    #print(proint(a,b))
    # print(proint([(1, 0), (0, 1), (1, -3)], [(2, 1), (0, 1), (2, 0)]))
    # print(norma(a))
    # print(dista([(2, 1)], [(-3, 2)]))
    #print(hermi([[(0, 2), (0, 0)], [(0, 0), (0, -2)]]))
    #print(uni([[(0, 2), (0, 0)], [(0, 0), (0, -2)]]))
    # a = (2, 2)
    # b = (2,2)
