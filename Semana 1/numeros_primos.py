# Mostrar los números primos entre 1 y 1000.

for i in range(1, 1000):
    primo = True
    j = 2
    while (i > j) and (primo == True):
        if i % j == 0:
            primo = False
            break
        else:
            j = j + 1

    if primo == True:
        print(i, "es primo")
