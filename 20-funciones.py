# ----------------------------
# Función sin argumentos
# ----------------------------
def funcion_sin_argumentos():
    """Función que no recibe ningún argumento."""
    print("Llamada a funcion_sin_argumentos")

funcion_sin_argumentos()

# ----------------------------
# Función con argumentos normales
# ----------------------------
def funcion_argumentos_normales(a, b, c):
    """Función con argumentos normales obligatorios."""
    print(f"Llamada a funcion_argumentos_normales con a={a}, b={b}, c={c}")

funcion_argumentos_normales(1, 2, 3)

# ----------------------------
# Función con argumentos por defecto
# ----------------------------
def funcion_argumentos_defecto(a=1, b=2):
    """Función con argumentos que tienen valores por defecto."""
    print(f"Llamada a funcion_argumentos_defecto con a={a}, b={b}")

funcion_argumentos_defecto()
funcion_argumentos_defecto(10)
funcion_argumentos_defecto(10, 20)

# ----------------------------
# Función con *args (tupla de argumentos posicionales variables)
# ----------------------------
def funcion_args(*args):
    """Función que recibe cualquier cantidad de argumentos posicionales."""
    print(f"Llamada a funcion_args con args={args}")

funcion_args(1, 2, 3)
funcion_args(10)

# ----------------------------
# Función con **kwargs (diccionario de argumentos con nombre variables)
# ----------------------------
def funcion_kwargs(**kwargs):
    """Función que recibe cualquier cantidad de argumentos con nombre."""
    print(f"Llamada a funcion_kwargs con kwargs={kwargs}")

funcion_kwargs(a=1, b=2, c=3)
funcion_kwargs(name="Juan", age=25)

# ----------------------------
# Función con combinación de argumentos
# ----------------------------
def funcion_combinada(a, b=2, *args, c, d=4, **kwargs):
    """
    Función que combina:
    - argumentos normales
    - argumentos con valor por defecto
    - *args (posicionales variables)
    - argumentos keyword-only (c, d)
    - **kwargs (argumentos con nombre variables)
    """
    print(f"Llamada a funcion_combinada con a={a}, b={b}, args={args}, c={c}, d={d}, kwargs={kwargs}")

funcion_combinada(1, 3, 4, 5, c=6, d=7, x=100)
