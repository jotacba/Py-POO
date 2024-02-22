#la enumeracion limita, restringe la cantidad de posibilidades de ciertos atributos
#en nuestro ejemplo tenemos el atributo tipo y solo 2opciones validas: vertebrado o invertebrado

from enum import Enum

class Tipo(Enum):
    VERTEBRADO = "vertebrado"
    INVERTEBRADO = "invertebrado"

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    #luego de crear los atributos con el constructor de la clase, creamos unmetodo para
    #mostrar cualquier animal (perro, gato, vaca, cerdo, etc.) mas adelante.
    #Esto es necesario cuando trabajamos con herencia, por eso usamos pass. 
    #los hijos seran los encargados de tener la logica de ese metodo
    
    def mostrarAnimal(self):
        pass
    #def getCantidadPatas(self):
    #    return self.cantidad_patas
    
    #def getTipo(self):
    #    return self.tipo
    
    def comer(self):
        pass
        #print("estoy comiendo")
    #todos los metodos que pueden definirse mejor dependiendo de cada animal deben definirse en cada caso


    #cuando creamos la clase hija que hereda atributos y metodos de la clase padre: definimos todos los atributos
    #y despues para no agregar todas las variables una a una usamos super que contiene los atributos de la 
    #clase padre y solamente agregamos las variables que faltan y son de la clase hija
class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def mostrarAnimal(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')
        print(f'Nombre: {self.nombre}')
        print(f'Raza: {self.raza}')

    def comer(self):
        print(f'Estoy comiendo alimento balanceado Dog Price, ñam ñam')
    
    def correr(self):
        print("estoy corriendo")

class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)
    
    def mostrarAnimal(self):
        #return super().mostrarAnimal()
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')

    def comer(self):
        print(f'Estoy comiendo serpientes y lauchas')
    
    def volar(self):
        print("estoy volando")

print("-----------------------------------------------")
print("Datos de un perro")
perro1 = Perro(4, Tipo.VERTEBRADO.value, "palavecino", "burrazo")
print("info adicional del perro")
perro1.mostrarAnimal()
perro1.comer()
perro1.correr()
print("------------------------------------------------")
print("datos del aguila")
aguila1 = Aguila(2, Tipo.VERTEBRADO.value)
print("info adicional del aguila")
aguila1.mostrarAnimal()
aguila1.comer()
aguila1.volar()