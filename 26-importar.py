
# 1) Importar el módulo completo
# Se accede usando el nombre del módulo
import math

resultado1 = math.sqrt(16)
valor_pi = math.pi


# 2) Importar funciones o variables específicas
# Se usan directamente sin el nombre del módulo
from math import sqrt, pi

resultado2 = sqrt(25)
valor_pi_2 = pi


# 3) Importar TODO el contenido del módulo
# (no recomendado en proyectos grandes)
from math import *

resultado3 = sqrt(36)
valor_pi_3 = pi


# 4) Importar un módulo con un alias (renombrar)
# Útil cuando el nombre es largo
import math as m

resultado4 = m.sqrt(49)
valor_pi_4 = m.pi


# 5) Importar funciones específicas con alias
from math import sqrt as raiz, pi as PI

resultado5 = raiz(64)
valor_pi_5 = PI
