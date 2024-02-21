    #Programacion orientada a objetos
    #las clases son los moldes a partir de los cuales se crean o instancian objetos
    #tienen atributos y metodos. los 1ros son caracteristicas que los definen y los segundos
    #son cosas que pueden hacer
    #Ejemplo: primer molde vehiculo. De ahi nacen auto, moto, barco y avion que "heredan" los atributos de
    #vehiculo
''' 
        Vehiculo
            marca
            modelo
            anio
            color
            precio
            patente
                acelerar
                frenar
            Auto
                cantPuertas
                tipoCombustible
            Moto
                ponerCasco
                sacarCasco
            Barco
                anclar
            Avion
                despegar
'''

from typing import Any


class Auto:
    #atributos
    def __init__(self, marca, modelo, anio, color, precio, patente, estado, motorPrendido):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.precio = precio
        self.patente = patente
        self.estado = estado
        self.motorPrendido = motorPrendido
    #Metodos, comportamientos, acciones
    #getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getAnio(self):
        return self.anio
    def getColor(self):
        return self.color
    def getPrecio(self):
        return self.precio
    def getPatente(self):
        return self.patente
    def getEstado(self):
        return self.estado
    def getMotorPrendido(self):
        return self.motorPrendido
    
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()}')
        print(f'Modelo: {self.getModelo()}')
        print(f'Anio: {self.getAnio()}')
        print(f'Color: {self.getColor()}')
        print(f'Precio: {self.getPrecio()}')
        print(f'Patente: {self.getPatente()}')
        print(f'Estado: {self.getEstado()}')
        print(f'Motor Prendido: {self.getMotorPrendido()}')

    def repararAuto(self):
        if(self.estado == "daniado"):
            print("se esta arreglando")
            self.estado = "funcionando"
            print("ya funciona")
        else:
            print("no hace falta arreglarlo")

    def modificarEstadoMotor(self):
        if(self.motorPrendido):
            print("el motor esta prendido, lo apago")
            self.motorPrendido = False
            print("lo apague")
        else:
            print("el motor esta apagado, lo prendo")
            self.motorPrendido = True
            print("lo prendi")

auto1 = Auto("fiat", "600", "1980", "rojo", "usd 500", "ASD123", "daniado", False)
auto2 = Auto("ferrari", "cheto", "2023", "verde", "usd 100000", "91218", "funcionando", True)

auto1.repararAuto()
auto2.repararAuto()

auto1.modificarEstadoMotor()
auto2.modificarEstadoMotor()

auto1.mostrarAuto()