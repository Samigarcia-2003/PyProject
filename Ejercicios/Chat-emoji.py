seguirChat = True
while seguirChat:
    texto = input(" ")
    if texto == 'salir':
        seguirChat = False
    text = texto.replace(':)', '😄')
    text = texto.replace(';-;', '😭')
    text = texto.replace(':3', '😇')
    text = texto.replace(':b', '😘')
    text = texto.replace(':d', '😈')
    text = texto.replace(':p', '🤡')
print(texto)