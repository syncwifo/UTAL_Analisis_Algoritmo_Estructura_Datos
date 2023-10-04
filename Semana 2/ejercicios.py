# def escribe_media(a, b):
#     media = (a + b) / 2
#     print(f"La media de {a} y {b} es: {media}")
#     return


# def calcula_media_desviacion(arreglo):
#     total = 0
#     for i in arreglo:
#         total += i
#     media = total / len(arreglo)
#     total = 0
#     for i in arreglo:
#         total += (i - media) ** 2
#     desviacion = (total / len(arreglo)) ** 0.5
#     return media, desviacion


# def exite(elemento, arreglo):
#     control = False
#     for i in arreglo:
#         if elemento == arreglo[i]:
#             control = True
#     return control


# def buscar_indice(elemento, arreglo):
#     indice = 0
#     for i in range(0, len(arreglo)):
#         if elemento == arreglo[i]:
#             indice = i

#     return indice


# def cifrado(palabra, clave):
#     letras = "abcdefghijklmnñopqrstuvxyz"
#     aux = ""
#     for letra in palabra:
#         indice = buscar_indice(letra, letras)
#         nueva_letra = letras[(indice + clave) % 26]
#         aux = aux + nueva_letra
#     return aux


# print(cifrado("z", 1))



from random import *

def matriz_random(m, n):

    m = [[randint(1, 7) for j in range(m)] for i in range(n)]

    for f in m:
        print(f)


matriz_random(10,10)