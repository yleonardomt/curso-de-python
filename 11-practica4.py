# Lista de platos
platos = ["Paella", "Risotto", "Sushi", "Tacos", "Pizza"]

# Tupla de precios correspondiente a cada plato
precios = (15, 12, 20, 10, 8)

# Slicing: seleccionar del segundo al cuarto plato
platos_seleccionados = platos[1:4]

# Diccionario del menú combinando platos y precios
menu = {
    "Paella": 15,
    "Risotto": 12,
    "Sushi": 20,
    "Tacos": 10,
    "Pizza": 8
}

# Imprimir el menú completo
print("Bienvenidos a nuestro menú especial:\n")
for plato, precio in menu.items():
    print(f"- {plato}: {precio} euros")
print()

# Indexing: obtener el tercer plato y su precio
tercer_plato = platos[2]            # índice 2 → tercer elemento
precio_tercer_plato = precios[2]    # variable correcta según la prueba
print(f"El tercer plato es {tercer_plato} y su precio es {precio_tercer_plato}.\n")

# Stride: seleccionar los platos en posiciones pares
platos_pares = platos[0::2]  # índice 0, 2, 4...
print(f"Los platos pares son: {platos_pares}")
