# El * se coloca para que la cantidad de argumentos que pasamos sean irrelevantes y los ejecute todos.
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 45, 32)
