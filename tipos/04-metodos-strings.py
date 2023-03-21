animal = "  chanchito feliz  "
print(animal.upper())
print(animal.lower())
# podemos con una variable o str usar los metodos que necesitemos
print(animal.strip().capitalize())
print(animal.title())
# si le agregas una l quita los espacios de la izquierda y una r para los de la derecha
print(animal.strip())
print(animal.find("feliz"))  # este es para indice
print(animal.replace("feliz", "lindo"))
# Por logica, el metodo de replace necesita dos argumentos o condiciones para ejecutarse
print("feliz" in animal)  # este es para booleano
# este es para booleano y busca si no esta en el str
print("feliz" not in animal)
