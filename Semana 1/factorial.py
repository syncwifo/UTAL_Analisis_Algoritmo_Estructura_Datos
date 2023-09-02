# Implementar una función que calcule el Factorial de un número dado.

def factorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado = resultado * i
        return resultado
