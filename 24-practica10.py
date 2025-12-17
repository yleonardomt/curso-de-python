# Clase Vulnerabilidad
class Vulnerabilidad:
    """
    Representa una vulnerabilidad identificada durante un ejercicio de Hacking Ético.
    
    Atributos:
        nombre (str): Nombre de la vulnerabilidad.
        severidad (str): Nivel de severidad (Baja, Media, Alta, Crítica).
        descripcion (str): Breve descripción de la vulnerabilidad.
    """
    def __init__(self, nombre, severidad, descripcion):
        self.nombre = nombre
        self.severidad = severidad
        self.descripcion = descripcion

    def mostrar_info(self):
        """Muestra la información de la vulnerabilidad."""
        print(f"\nNombre: {self.nombre}")
        print(f"Severidad: {self.severidad}")
        print(f"Descripción: {self.descripcion}")

    def recomendar_acciones(self):
        """Proporciona recomendaciones basadas en la severidad."""
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


# --- Creación de objetos ---
vuln1 = Vulnerabilidad("SQL Injection", "Alta", "Permite la ejecución de consultas SQL no autorizadas.")
vuln2 = Vulnerabilidad("XSS", "Media", "Permite la ejecución de scripts en el navegador del usuario.")
vuln3 = Vulnerabilidad("Desbordamiento de Buffer", "Crítica", "Permite la ejecución arbitraria de código.")

# Lista de registro de vulnerabilidades
registro_vulnerabilidades = [vuln1, vuln2, vuln3]

# Recorrer la lista y mostrar información y recomendaciones
for vulnerabilidad in registro_vulnerabilidades:
    vulnerabilidad.mostrar_info()
    vulnerabilidad.recomendar_acciones()
