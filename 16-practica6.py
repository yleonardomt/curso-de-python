# Tupla con los niveles de amenaza
niveles_amenaza = ("bajo", "moderado", "alto", "crítico")

# Nivel de amenaza actual
amenaza_actual = "bajo"

# Comprobar si el nivel de amenaza es válido
if amenaza_actual in niveles_amenaza:
    # Recomendaciones según el nivel
    if amenaza_actual == "bajo":
        accion = "Realizar auditorías de seguridad regulares."
    elif amenaza_actual == "moderado":
        accion = "Reforzar la concienciación de los empleados sobre riesgos de Ciberseguridad."
    elif amenaza_actual == "alto":
        accion = "Implementar medidas de seguridad adicionales y revisar accesos."
    elif amenaza_actual == "crítico":
        accion = "Activar el protocolo de respuesta a incidentes."
else:
    accion = "Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico)"

# Mostrar resultados
print("Nivel de amenaza actual:", amenaza_actual)
print("Actividad recomendada:", accion)
