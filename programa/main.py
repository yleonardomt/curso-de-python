# 1️ Importando el módulo completo
import modulo1

modulo1.test()  # función
print(modulo1.VERSION)  # constante
print(modulo1.incrementar_contador())  # variable global

obj1 = modulo1.Test("Router1")  # clase Test
obj1.saludo()

calc = modulo1.Calculadora()  # clase Calculadora
print(calc.sumar(10, 5))
print(calc.restar(10, 5))

# 2️ Importando elementos específicos
from modulo1 import sumar, Test

print(sumar(7, 8))  # función importada
obj2 = Test("Switch1")
obj2.saludo()

import paquetes.modulo2