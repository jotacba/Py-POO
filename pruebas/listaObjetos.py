class Jugador:
    def __init__(self, nombre, edad, altura, posicion):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.posicion = posicion

equipo = []

equipo.append(Jugador("Franco Mastantuono", 16, "181 cm", "Volante Ofensivo"))
equipo.append(Jugador("Ian Subiabre", 17, "172 cm", "Extremo Izquierdo"))
equipo.append(Jugador("Agustin Ruberto", 18, "182 cm", "Centrodelantero"))

for jugador in equipo:
    print(f'Jugador: {jugador.nombre}')

#podemos acceder directamente a los atributos de cada objeto en la lista
print(equipo[0].edad)
print(equipo[2].posicion)