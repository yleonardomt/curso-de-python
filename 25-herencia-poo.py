# Clase base Vulnerabilidad
class Vulnerabilidad:
    """
    Clase base que representa una vulnerabilidad genérica.
    """
    def __init__(self, nombre, severidad, descripcion):
        self.nombre = nombre
        self.severidad = severidad
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Severidad: {self.severidad}")
        print(f"Descripción: {self.descripcion}")

    def recomendar_acciones(self):
        if self.severidad == "Crítica":
            recomendacion = "Aplicar parches de seguridad inmediatamente y revisar sistemas afectados."
        elif self.severidad == "Alta":
            recomendacion = "Realizar una auditoría de seguridad y aplicar medidas correctivas lo antes posible."
        elif self.severidad == "Media":
            recomendacion = "Monitorear la actividad del sistema y planificar la aplicación de parches."
        elif self.severidad == "Baja":
            recomendacion = "Mantener bajo observación y revisar en el próximo ciclo de actualización."
        else:
            recomendacion = "Severidad desconocida. Revisar manualmente."
        print(f"Acción recomendada: {recomendacion}")


# Clase hija para vulnerabilidades web
class VulnerabilidadWeb(Vulnerabilidad):
    """
    Representa vulnerabilidades específicas de aplicaciones web.
    """
    def __init__(self, nombre, severidad, descripcion, url_afectada):
        super().__init__(nombre, severidad, descripcion)
        self.url_afectada = url_afectada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"URL afectada: {self.url_afectada}")


# Clase hija para vulnerabilidades de red
class VulnerabilidadRed(Vulnerabilidad):
    """
    Representa vulnerabilidades específicas de la red.
    """
    def __init__(self, nombre, severidad, descripcion, ip_afectada):
        super().__init__(nombre, severidad, descripcion)
        self.ip_afectada = ip_afectada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"IP afectada: {self.ip_afectada}")


# --- Creación de objetos ---
vuln_web1 = VulnerabilidadWeb("XSS", "Media", "Permite la ejecución de scripts en el navegador del usuario.", "http://example.com/login")
vuln_web2 = VulnerabilidadWeb("SQL Injection", "Alta", "Permite la ejecución de consultas SQL no autorizadas.", "http://example.com/search")
vuln_red = VulnerabilidadRed("Desbordamiento de Buffer", "Crítica", "Permite la ejecución arbitraria de código.", "192.168.1.10")

# Lista de todas las vulnerabilidades
registro_vulnerabilidades = [vuln_web1, vuln_web2, vuln_red]

# Recorrer la lista y mostrar info y recomendaciones
for vulnerabilidad in registro_vulnerabilidades:
    vulnerabilidad.mostrar_info()
    vulnerabilidad.recomendar_acciones()
