# ----------------------
# Gestión de fondos con WHILE
# ----------------------

fondos = 10000
acciones = [2000, -500, 300, -50]
indice = 0

print(f"Fondos iniciales: {fondos}")

while indice < len(acciones):
    accion_actual = acciones[indice]

    if accion_actual < 0 and abs(accion_actual) > fondos:
        print(f"Acción omitida por insuficiente fondos: {accion_actual}")
    else:
        fondos += accion_actual
        print(f"Acción procesada: {accion_actual}. Fondos actuales: {fondos}")
    
    indice += 1

print(f"Fondos finales después de las acciones: {fondos}")
