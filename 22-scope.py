# ------------------------
# Scope en Python - Ejemplo completo
# ------------------------

# Variable global
global_var = 100

def funcion_exterior():
    # Variable enclosing (función contenedora)
    enclosing_var = 10

    def funcion_interior():
        # Variable local
        local_var = 5

        # Accediendo a variables de distintos scopes
        print("Local variable:", local_var)          # Local
        print("Enclosing variable:", enclosing_var)  # Enclosing
        print("Global variable:", global_var)        # Global
        print("Built-in function len():", len([1,2,3])) # Built-in

        # Modificando enclosing_var usando nonlocal
        nonlocal enclosing_var
        enclosing_var += 1
        print("Enclosing variable modificada:", enclosing_var)

        # Modificando global_var usando global
        global global_var
        global_var += 50
        print("Global variable modificada:", global_var)

    funcion_interior()

    # Verificando el cambio en enclosing_var
    print("Enclosing variable fuera de interior:", enclosing_var)

# Llamada a la función exterior
funcion_exterior()

# Verificando el cambio en global_var
print("Global variable fuera de funciones:", global_var)
