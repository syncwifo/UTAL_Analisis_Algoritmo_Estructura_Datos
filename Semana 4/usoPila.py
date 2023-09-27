from pila import Pila, apilar, desapilar, imprimir

pila = Pila()

apilar(pila, "primero")
apilar(pila, "segundo")
apilar(pila, "tercero")
print("------ despues de apilar")
imprimir(pila)

desapilar(pila)
print("------ despues de desapilar")
imprimir(pila)
