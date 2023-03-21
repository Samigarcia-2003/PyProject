mascotas = [
    "Pelusa", 
    "pulga", 
    "Junior", 
    "Chanchito feliz", 
    "kitty",
    "Pulga"
]
mascotas.insert(3, "Pecas")
mascotas.append("Antonio")#append para agregar elemento al final de la lista

mascotas.remove("pulga")#remover elemento
mascotas.pop(4)#eliminar el ultimo elemento si no hay un indice como parametro
del mascotas[4]#eliminar elemento con indice
mascotas.clear()#eliminar todo el contenido
print(mascotas)