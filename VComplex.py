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

def Accion (a, b):
    n,m = len(a),len(a[0])
    B = len (b)
    c = []
    if B == m:
        S = (0,0)
        for i in range (n):
            for j in range (m):
                p = multiplicacion (a[i][j], b[j])
                S = Suma (S, p)
            c = c + [S]
            S = (0,0)
    return c

# Producto interno de dos vectores

def ProductIntVec (a, b):
    c = (0,0)
    for i in range (len(a)):
        n = nc.producplx((conjumatriz(a[i]), b[i]))
        c = nc.sumacplx(c, n)
    return c

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
    matr = proma(dagamatriz(a), a)
    ident = iden(len(a), len(a[0]))
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
def tensor(a, b):
    r = []
    m = 0
    n = 0
    while m < ((len(a) - 1) * 2):
        f1 = a[m]
        f2 = b[n]
        aux = []
        for i in f1:
            for j in f2:
                aux = aux + [nc.producplx(i, j)]
        m = m + 1
        f2 = b[n]
        r = r + [aux]
        aux = []
        for i in f1:
            for j in f2:
                aux = aux + [nc.producplx(i, j)]
        m = m + 1
        n = n - 1
        r = r + [aux]
    return r
# -----------------------------------------------------------------------------------------------------------------------
def conjucplx2(a):
    real = a[0] * 1
    img = a[1] * -1
    return (real, img)

def iden(m,n):
    c = [[(0, 0) for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j:
                c[i][j] = ((2 / 2), 0)
    return c

def multvxm(a,b):
    re = [(0, 0) for j in range(len(a))]
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            re[i] = nc.producplx(a[i], b)
    return re

def matrixTrans (a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = a [j][i]
    return c

def matrixConj (a):
    n,m = len(a),len(a[0])
    i = 0
    j = 0
    c = [[0 for j in range (m) ]for i in range (n)]
    for i in range (n):
            for j in range (m):
                c[i][j] = conj (a[i][j])
    return c

def matrixAdj (a):
    c = matrixTrans (matrixConj (a))
    return c

def multiMatrix (a, b):
    n,m = len(a),len(a[0])
    N,M = len(b), len(b[0])
    c = [[(0,0) for j in range (m) ]for i in range (n)]
    if m == N :
        for i in range (n):
            for j in range (M):
                for k in range (N):
                    p = multiplicacion (a[i][k], b[k][j])
                    q = c [i][j]
                    c[i][j] = Suma (p, q)

    return c
def transito(a,b):
    r = ProductIntVec(b,a)
    return r

# -----------------------------------------------------------------------------------------------------------------------