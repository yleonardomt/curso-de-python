# Lista de letras del alfabeto en mayúsculas
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Función de cifrado César
def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nuevo_indice = (indice + desplazamiento) % len(alfabeto)
            texto_cifrado += alfabeto[nuevo_indice]
        elif letra in [' ', ',', '.', ':']:
            texto_cifrado += letra
        else:
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_cifrado

# Función de descifrado César
def descifrado_cesar(texto, desplazamiento):
    texto_descifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nuevo_indice = (indice - desplazamiento) % len(alfabeto)
            texto_descifrado += alfabeto[nuevo_indice]
        elif letra in [' ', ',', '.', ':']:
            texto_descifrado += letra
        else:
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_descifrado

# ----------------------
# Pruebas de la práctica
# ----------------------

# Texto original
texto = "HOLA MUNDO."
desplazamiento = 3

# Cifrado
texto_cifrado = cifrado_cesar(texto, desplazamiento)
print("Texto plano:", texto)
print("Texto cifrado:", texto_cifrado)

# Descifrado
texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)
print("Texto cifrado:", texto_cifrado)
print("Texto descifrado:", texto_descifrado)

# Prueba con minúsculas (debe devolver mensaje de error)
error = cifrado_cesar("Hola Mundo.", desplazamiento)
print(error)
