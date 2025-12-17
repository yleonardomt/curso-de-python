x = 10
y = 3.5
z = x + y
s = "hola"
b = True

if x > 5:
    r = "mayor"
elif x == 5:
    r = "igual"
else:
    r = "menor"

for i in range(3):
    print(i)

while x > 0:
    x -= 1

def suma(a, b):
    return a + b

resultado = suma(2, 3)

lista = [1, 2, 3]
tupla = (4, 5, 6)
conjunto = {1, 2, 3}
diccionario = {"a": 1, "b": 2}

cuadrados = [i*i for i in range(5)]
pares = {i for i in range(10) if i % 2 == 0}
mapa = {i: i*i for i in range(3)}

f = lambda a, b: a * b
v = f(2, 4)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        return "Hola " + self.nombre

p = Persona("Ana")

try:
    n = int("10")
except ValueError:
    n = 0
finally:
    n += 1

def contador():
    i = 0
    while True:
        yield i
        i += 1

c = contador()
next(c)

import math
valor = math.sqrt(16)

async def tarea():
    return 1
