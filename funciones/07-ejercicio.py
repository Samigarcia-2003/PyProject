def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palidromo(texto): 
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palidromo("amo la paloma"))
print(es_palidromo("abba"))
print(es_palidromo("reconocer"))
print(es_palidromo("recordar"))
print(es_palidromo("gato"))
