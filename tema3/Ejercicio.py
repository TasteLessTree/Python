class Jugador:
    def __init__(self, nombre, dorsal, posicion):
        self.nombre = nombre
        self.dorsal = dorsal
        self.posicion = posicion

    def describirse(self):
        print(f'Soy {self.nombre}, llevo el {self.dorsal} y juego de {self.posicion}')

class Equipo:
    def __init__(self, nombre_equipo, color_camisa, total_balones):
        self.nombre_equipo = nombre_equipo
        self.color_camisa = color_camisa
        self.total_balones = total_balones
        self.lista_jugadores = []
        self.__balones_disponibles = self.total_balones

    def fichar_jugador(self, jugador):
        self.lista_jugadores.append(jugador)
        print(f'Se ha fichado {jugador.nombre} para {jugador.posicion}')

    def mostrar_plantilla(self):
        for jugador in self.lista_jugadores:
            jugador.describirse()
            print('--------------------------------------------')

    def iniciar_entrenamiento(self, cantidad_necesaria):
        if cantidad_necesaria > self.__balones_disponibles:
            print(f'Error, no hay balones sufientes. {cantidad_necesaria} > {self.__balones_disponibles}')
        else:
            self.__balones_disponibles -= cantidad_necesaria
            print('El entranamiento va a empezar...')


    def fin_entrenamiento(self, cantidad_devuelta):
        nuevos_balones = cantidad_devuelta + self.__balones_disponibles

        if nuevos_balones > self.total_balones:
            print(f'Error. Hay más balones con respecto a la cantidad original. {nuevos_balones} > {self.__balones_disponibles}')
        else:
            self.__balones_disponibles = nuevos_balones
            print('Entrenamiento finalizado.')

if __name__ == "__main__":
    equipo = Equipo("Red FC", "Roja", 10)
    jugador1 = Jugador("Messi", 10, "Delantero")
    jugador2 = Jugador("Marco", 1, "Portero")
    jugador3 = Jugador("Mario", 12, "Centro")

    equipo.fichar_jugador(jugador1)
    equipo.fichar_jugador(jugador2)
    equipo.fichar_jugador(jugador3)
    equipo.mostrar_plantilla()

    equipo.iniciar_entrenamiento(12)
    equipo.iniciar_entrenamiento(5)
    equipo.fin_entrenamiento(5)