# Implementar una función que calcule el Factorial de un número dado. Recursiva


def factorialRecursivo(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return factorialRecursivo(numero - 1) * numero


print(factorialRecursivo(999))