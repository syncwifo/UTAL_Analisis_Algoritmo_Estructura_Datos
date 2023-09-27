from cola import Cola, arribo, atencion, imprimir

cola = Cola()

arribo(cola, "primero")
arribo(cola, "segundo")
arribo(cola, "tercero")
print("------ despues de arribar")
imprimir(cola)

atencion(cola)
print("------ despues de atender")
imprimir(cola)
