# Variables principales del astronauta
nombre_astronauta = "Max"  # Nombre del astronauta
edad_astronauta = 25       # Edad en años
destino = "Marte"          # Planeta al que se dirige

# Variables de navegación
combustible = 85            # Porcentaje de combustible restante
velocidad = 27000           # Velocidad de viaje en km/s

# Cabecera del diario
print("Diario de un Astronauta\n")  # Presentación del diario con salto de línea

# Mensaje de presentación usando f-strings para insertar variables
print(f"Hola, soy {nombre_astronauta}, tengo {edad_astronauta} años y mi próximo destino es {destino}.\n")

# Mensaje de navegación usando f-strings para mostrar velocidad y combustible
print(f"Estoy navegando a {velocidad} km/s con {combustible}% de combustible restante hacia {destino}.\n")

# Entrada del día 1
print("Fecha: 2024-01-10")  # Fecha de la primera entrada
print("Hoy experimentamos con el cultivo de plantas en microgravedad.")  # Descripción del día
print("Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!\n")  # Mensaje personal con salto de línea

# Entrada del día 2
print("Fecha: 2024-01-11")  # Fecha de la segunda entrada
print("Realizamos una caminata espacial para reparar un panel solar.")  # Descripción del día
print("Mensaje personal: Flotar en el espacio nunca deja de asombrarme.\n")  # Mensaje personal con salto de línea

# Comentarios agregados para explicar:
# 1. Por qué se usan variables: para modificar fácilmente información del astronauta y del viaje.
# 2. Por qué se usan f-strings: para insertar valores de variables dentro de los mensajes sin concatenar.
# 3. Por qué se agregan saltos de línea: para mejorar la legibilidad del diario.
# 4. Organización de entradas: cada día tiene fecha, descripción y mensaje personal para simular un diario real.
