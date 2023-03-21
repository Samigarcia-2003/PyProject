numeros = [2, 4, 6, 45, 76, 22]

"""numeros.sort(reverse=True) #sort para imprimir la lista en orden acendente y reverse para decendente
num = sorted(numeros) #crea una nueva lista ordenada
print(numeros)
print(num)"""

usuario = [
    ["Sam", 7],
    ["Kitty", 10],
    ["Junior", 1]
]

#usuario.sort(key=ordena)#por si solo, la funcion no funciona con parametros necesitas anteponer el key

usuario.sort(key=lambda elem: elem[1]) #la función lambda nos ahorra el tener que crear una función
print(usuario)
