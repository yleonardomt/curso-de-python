
def verificar_disponibilidad(hosts):
    """
    Función que recibe una lista de IPs (hosts)
    y devuelve un diccionario indicando si cada host está disponible o no.
    """
    resultados = {}  # Diccionario vacío para almacenar resultados
    
    for host in hosts:
        # Verifica si los tres primeros dígitos de la IP son "192"
        if host.startswith("192"):
            resultados[host] = "Disponible"
        else:
            resultados[host] = "No disponible"
    
    return resultados
