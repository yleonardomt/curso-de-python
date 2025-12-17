# -----------------------------
# módulo1.py
# Ejemplo completo de módulo en Python
# -----------------------------

# Constantes (nombres en mayúsculas)
VERSION = "1.0"
AUTOR = "Yhonatan"

# Variables globales
contador = 0

# -----------------------------
# Funciones
# -----------------------------

def test():
    """Función simple de prueba"""
    print("Estoy en modulo1")

def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

def incrementar_contador():
    """Incrementa la variable global contador"""
    global contador
    contador += 1
    return contador

# -----------------------------
# Clases
# -----------------------------

class Test:
    """Clase de ejemplo"""
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        print(f"Hola, soy {self.nombre}")

class Calculadora:
    """Clase para operaciones matemáticas"""
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        return self.resultado

# -----------------------------
# Código de prueba (solo se ejecuta si corro este archivo directamente)
# -----------------------------
if __name__ == "__main__":
    test()
    print("Versión:", VERSION)
    c = Calculadora()
    print("Suma:", c.sumar(5, 3))
