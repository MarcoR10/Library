import Ncomplex as nc
def svecto(a,b):
    num = len(a)
    suma = [(0,0)for i in range(num)]
    for i in range(0,num):
        suma[i] = nc.sumacplx(a[i],b[i])
    return suma
def invecto(a):
    num = len(a)
    inv = a
    for i in range(0,num):
        inv[i] = inv[i]*(-1)
    return inv
if __name__ == '__main__':
    a = [(2,3),(4,3),(7,9)]
    b = [(2,3),(4,3),(6,8)]
    print(svecto(a,b))
    print(invecto(a))