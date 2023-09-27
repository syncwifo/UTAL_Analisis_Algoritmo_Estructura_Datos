# Variable dinámica: una variable dinámica es aquella que se puede crear y destruir en tiempo de ejecución 
# a diferencia de una variable estática que lo hace en tiempo de compilación. 
# Este tipo de variables son administradas mediante el uso de punteros.

# Puntero: el puntero es un tipo de dato que se utiliza para almacenar una dirección de memoria de una variable dinámica
# –es decir se podría decir que un puntero apunta a una variable dinámica– esto también se conoce como dirección de referencia.

# Nodo: es un tipo de datos que se define mediante el uso de una clase 
# –dado que en Python no existen los registros– para representar a cada elemento de nuestra estructura de datos. 
# Dependiendo de esta pueden variar sus atributos, pero en su esencia un nodo debe tener mínimamente 
# un campo donde se almacene la información y otro que lo enlace con el siguiente o anterior nodo de la estructura.

# Variables huérfanas: cuando una variable dinámica deja de ser apuntada por un puntero, 
# quedará en memoria pero no podrá accederse a ella porque su dirección se perdió. 
# En Python cuando ocurre esto el intérprete elimina automáticamente dicha variable para liberar espacio en memoria. 
# Por lo que para eliminar una variable dinámica solo basta con cambiar la dirección del puntero que la señala.

# Variables estáticas
num1 = 1
num2 = num1
num2 = num2 +3 
print(num2 == num1)

#Variables dinámicas
lista1 = [1,2,3,4]
lista2 = lista1
lista2[2]=8
print(lista1==lista2)

# Prueba de punteros

puntero1 = [1,0]
puntero2 = [1.0]

if(puntero1==puntero2):
    print('apuntan a la misma variable')
else:
    print('apuntan a diferentes variables')

puntero2={}
print(puntero2)
puntero2=puntero1

if(puntero1==puntero2):
    print('apuntan a la misma variable')
else:
    print('apuntan a diferentes variables')