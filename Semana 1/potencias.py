# Implementar una función para calcular la potencia dado dos números enteros,
# el primero representa la base y segundo el exponente.
#


def potencia(base, exponente):
    resultado = 1
    for i in range(1, exponente + 1):
        resultado = base * resultado

    return resultado
