numeros = [1, 2, 3]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros = numeros #Aquí elegimos el elemento que necesitamos mostrar fuera de la lista.
print(primero, otros)