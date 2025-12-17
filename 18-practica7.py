# ----------------------
# PARTE 1: Inventario
# ----------------------

inventario = [
    ("Nmap", 50, 0.5),
    ("Wireshark", 30, 0.3),
    ("Metasploit", 20, 0.4),
    ("Burp Suite", 15, 0.45)
]

valor_total = 0
mayor_cantidad = {"herramienta": "", "cantidad": 0, "precio": 0}

for herramienta, cantidad, precio in inventario:
    valor_total += cantidad * precio

    if cantidad > mayor_cantidad["cantidad"]:
        mayor_cantidad["herramienta"] = herramienta
        mayor_cantidad["cantidad"] = cantidad
        mayor_cantidad["precio"] = precio

print(f"Valor total del inventario: {valor_total} eur")
print(f"Herramienta con mayor cantidad de licencias: {mayor_cantidad['herramienta']} ({mayor_cantidad['cantidad']} unidades)")

# ----------------------
# PARTE 2: Compra
# ----------------------

compra = {"Nmap": 5, "Wireshark": 3}
precio_total = 0

for herramienta, cantidad, precio in inventario:
    if herramienta in compra:
        precio_total += compra[herramienta] * precio

print(f"Precio de la adquisición: {precio_total} eur")
