Peso = int(input('Ingrese su peso en kg '))
Alturacm = int(input('Ingrese su altura en cm '))
ALturaM = Alturacm / 100

imc = Peso / (ALturaM * ALturaM)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print("Estado de delgadez")
if imc >= 20 and imc < 26:
    print("Estado normal")
if imc >= 26 and imc < 30:
    print("Estado de sobrepeso")
if imc >= 30:
    print("Estado de obesidad")
