# ----------------------
# FOR con RANGE
# ----------------------
# Imprimir números del 1 al 5
for i in range(1, 6):  # range(inicio, fin) → fin no incluido
    print("Número:", i)

# ----------------------
# WHILE
# ----------------------
contador = 1
while contador <= 5:
    print("Contador:", contador)
    contador += 1  # aumentar contador para evitar bucle infinito

# ----------------------
# BREAK
# ----------------------
for i in range(1, 10):
    if i == 4:
        break  # sale del bucle cuando i es 4
    print("Break ejemplo:", i)

# ----------------------
# CONTINUE
# ----------------------
for i in range(1, 6):
    if i == 3:
        continue  # salta la iteración cuando i es 3
    print("Continue ejemplo:", i)

# ----------------------
# LISTAS e IN
# ----------------------
# Lista de tareas del día de un astronauta
tareas = ["alimentar plantas", "revisar paneles solares", "registrar experimentos", "comer", "hacer ejercicio"]

# Recorrer la lista con for
for tarea in tareas:
    print("Tarea pendiente:", tarea)

# Verificar si una tarea está en la lista usando in
if "hacer ejercicio" in tareas:
    print("¡No olvides hacer ejercicio hoy!")
else:
    print("No hay ejercicio programado.")
