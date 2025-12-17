# ----------------------
# Operadores de Pertenencia (in / not in)
# ----------------------
frutas = ["manzana", "banana", "cereza"]

esta_manzana = "manzana" in frutas    # True
no_kiwi = "kiwi" not in frutas       # True

# ----------------------
# Operadores Lógicos (and, or, not)
# ----------------------
a = True
b = False

and_logico = a and b   # False
or_logico = a or b     # True
not_logico = not a     # False

# ----------------------
# Operadores de Identidad (is / is not)
# ----------------------
x = [1, 2, 3]
y = x          # apunta a la misma lista
z = [1, 2, 3]  # lista distinta con mismos valores

mismo_objeto = x is y       # True
distinto_objeto = x is z    # False
no_es_mismo = x is not z    # True
