saludo = "Hola global"


def saludar():
    saludo = "Hi girl"
    print(saludo)

def saludachanchito():
    saludo = "Hola chanchito"
    print(saludo)


saludar()
saludachanchito()
print(saludo)

#Pese a que las variables tengan el mismo nombre no tienen mel mismo valor puesto que estan registradas dentro de distintas funciones
#no podemos utilizar una variable que este dentro de una función sin llamar a la función.
#Sin embargo, si se define una variable con el mismo nombre pero sin estar dentro de una función
#hace que esa variable tenga un alcance global, que es independiente de la función
#ten en cuenta que utilizar variables globales, a no se que sean estrictamente necesarias es una mala practica.