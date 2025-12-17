# main.py
# Programa principal que usa el módulo monitor.py

# Importamos la función del módulo
from monitor import verificar_disponibilidad

# Lista de hosts a monitorizar
hosts = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]

# Llamamos a la función del módulo y guardamos los resultados
resultados = verificar_disponibilidad(hosts)

# Imprimimos los resultados
for host, estado in resultados.items():
    print(f"Host: {host}, Disponibilidad: {estado}")
