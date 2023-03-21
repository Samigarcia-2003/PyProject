# utilizamos def para definir la función que queremos crear seguida del nombre que le daremos y terminando con ():
# lo que va entrre parentesis es obligatorio para que el llamado a la función se complete.
def hola():  # todo lo que vaya a incluir esta función va a ser indentado para saber que es parte de esta función
    print("Hola mundo!")
    print("Bienvenida Sami")


hola()


# En este caso la variable nombre es el parametro obligatorio para ejecutar el código.
def cliente(nombre):
    print("Pagina de inicio para clientes registrados")
    print(f"Bienvenido {nombre}")


# En el momento en que a la variable se le da un valor al hacer el llamado de la función
cliente("Sam")
# el paramentro deja de ser parametro y se convierte en argumento.


def equipo(grupo):  # Aqui es un parametro
    print("Bienvenidos a la pagina de inicio")
    print(f"Estan registradas en el {grupo}")


equipo("Grupo A")  # Aqui el parametro se vuelve argumento


def oficina(ubicación, disponibilidad):  # Esta es la forma correcta de poner mas parametros
    print("Pagina de inicio para clientes registrados")
    print(f"Tiene cita en {ubicación} a las {disponibilidad}")


oficina("Madrid", "12:50")  # esta es la forma correcta de recibir argumentos

# También podemos agregarle un valor por defecto a un parametro que cumpla en el argumento.
