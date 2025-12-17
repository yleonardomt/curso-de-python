# Clase base: Jugador
class Jugador:
    """
    Representa un jugador en un juego.
    
    Attributes:
        nombre (str): Nombre del jugador.
        puntos (int): Puntos acumulados del jugador.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0  # Atributo de instancia

    def agregar_puntos(self, puntos):
        """Agrega puntos al jugador."""
        self.puntos += puntos
        print(f"{self.nombre} ahora tiene {self.puntos} puntos.")

    def mostrar_info(self):
        """Muestra la información del jugador."""
        print(f"Jugador: {self.nombre}, Puntos: {self.puntos}")


# Subclase: JugadorVIP hereda de Jugador
class JugadorVIP(Jugador):
    """
    Jugador VIP con bonus extra por cada partida.

    Attributes:
        bono_vip (int): Puntos adicionales que recibe el jugador VIP.
    """
    def __init__(self, nombre, bono_vip=20):
        super().__init__(nombre)  # Llamamos al constructor de la clase base
        self.bono_vip = bono_vip

    def agregar_puntos(self, puntos):
        """
        Agrega puntos al jugador VIP incluyendo el bono extra.
        Sobrescribe el método de la clase base.
        """
        total = puntos + self.bono_vip
        self.puntos += total
        print(f"{self.nombre} (VIP) recibe {puntos} + {self.bono_vip} de bono = {total} puntos. Total: {self.puntos}")


# Clase para gestionar el juego
class Juego:
    """
    Representa un juego donde se registran puntos de los jugadores.
    
    Attributes:
        jugadores (list): Lista de jugadores en el juego.
    """
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        """Agrega un jugador a la lista del juego."""
        self.jugadores.append(jugador)
        print(f"{jugador.nombre} se ha unido al juego.")

    def mostrar_puntajes(self):
        """Muestra los puntajes de todos los jugadores."""
        print("\nPuntajes actuales de todos los jugadores:")
        for jugador in self.jugadores:
            jugador.mostrar_info()


# --- Ejemplo de uso ---
# Crear instancia de juego
mi_juego = Juego()

# Crear jugadores
juan = Jugador("Juan")
maria = JugadorVIP("Maria")  # VIP

# Agregar jugadores al juego
mi_juego.agregar_jugador(juan)
mi_juego.agregar_jugador(maria)

# Registrar puntos
juan.agregar_puntos(50)
maria.agregar_puntos(50)

# Mostrar puntajes finales
mi_juego.mostrar_puntajes()
