# Calcular la suma de los divisores de un número “M”.


def sumaDivisores(m):
    suma_divisores = 0
    for i in range(1, m):
        if m % i == 0:
            suma_divisores = suma_divisores + i
    return suma_divisores


print(sumaDivisores(10000))
