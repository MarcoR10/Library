# Marco alvarez
# Libreria de numeros complejos
# Esta funcion imprime la nomencaltura de numeros complejos
import math
def prettyprint(c):
    print(str(c[0]) + ' + ' + str(c[1]) + 'i')
# Esta funcion suma numeros complejos
def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

# Esta funcion multiplica numeros complejos
def producplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)

# Esta funcion resta numeros complejos
def restacplx(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return (real, img)

# Esta funcion divide numeros complejos
def divicioncplx(a, b):
    real1 = (a[0] * b[0]) + (a[1] * b[1])
    real2 = ((b[0] ** 2) + (b[1] ** 2))
    real = round(real1 / real2,2)
    img1 = (a[1] * b[0]) - (a[0] * b[1])
    img2 = ((b[0] ** 2) + (b[1] ** 2))
    img = round(img1 / img2,2)
    return (real, img)

# Esta funcion saca el modulo del numero introducido
def modulocplx(a,b):
    raiz = math.sqrt((a**2) + (b**2))
    resul = round(raiz, 2)
    return resul
# Esta funcion saca el conjugado del numero introducido
def conjucplx(a):
    Conjugado = (a[1] * (-1))
    return (a[0], Conjugado)
# Esta funcion convierte una representacion polar a cartesiana
def capcplx(a):
    modul = round(modulocplx(a[0],a[1]),2)
    fase = round(math.atan(a[1]/a[0]),2)
    return (modul,fase)

# Esta funcion convierte una representacion cartesiana a polar
def paccplx(a):
    real = round(a[0]*(math.cos(a[1])),2)
    img = round(a[0]*(math.sin(a[1])),2)
    return (real,img)
# Modulo
def modulo (a):
    rad = (a[0]**2) + (a[1]**2)
    mod = math.sqrt(rad)
    mod = round(mod, 2)
    return mod
if __name__ == '__main__':
    prettyprint(sumacplx((2, 3), (4, 7)))
    prettyprint(producplx((0, 2), (0, 2)))
    prettyprint(restacplx((2, 3), (4, 7)))
    prettyprint(divicioncplx((2, 3), (4, 7)))
    print(modulocplx((1/math.sqrt(2)), (7/math.sqrt(2))))
    prettyprint(conjucplx((2,3)))
    print(capcplx((2,3)))
    prettyprint(paccplx((2,0.52)))