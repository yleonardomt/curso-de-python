try:
    x = int(input("Número: "))          # convertir a entero
    y = 10 / x                          # división
except ValueError:
    print("No es un número")            # error de conversión
except ZeroDivisionError:
    print("División entre cero")        # dividir por 0
else:
    print(y)                            # sin errores
finally:
    print("Fin")                        # siempre se ejecuta


def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad inválida")   # lanzar error
    return True


try:
    validar_edad(-1)                    # provoca error
except ValueError as e:
    print(e)                            # mostrar error
