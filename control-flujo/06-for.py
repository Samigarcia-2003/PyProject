buscar = 10
for numero in range(5):  # siempre con range se imprimen la cantidad de numeros o caracteres puestos en el parentesis menos 1, es decir, si pones cinco se ejecutaran desde el cero hasta el 4
    print(numero)
    if numero == buscar:
        print("encontrar", buscar)
        break
else:
    print("No encontre el numero buscado :[")

for char in "Ulrimate Python":
    print(char)
