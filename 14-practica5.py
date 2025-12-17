# Definir la contraseña
password = "Testpass1234"

# Verificar criterios
longitud = len(password) >= 8               # al menos 8 caracteres
caracter = "@" not in password and "#" not in password  # no contiene @ ni #
numero = any(char.isdigit() for char in password)       # contiene al menos un número
espacios = " " not in password                             # no contiene espacios

# Comprobar si cumple todos los criterios usando operador lógico AND
segura = longitud and caracter and numero and espacios

# Mostrar resultados
print("Contraseña:", password)
print("¿La contraseña cumple con los criterios establecidos?", segura)
