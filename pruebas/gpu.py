from enum import Enum

class Fabricante(Enum):
    NVIDIA = "NVIDIA"
    AMD = "AMD"
    SAMSUNG = "SAMSUNG"
    MOTOROLA = "MOTOROLA"

class Condicion(Enum):
    NUEVO = "Nuevo"
    USADO = "Usado"


class Hardware:
    def __init__(self, fabricante, condicion, estado, color, precio):
        self.fabricante = fabricante
        self.condicion = condicion
        self.estado = estado
        self.color = color
        self.precio = precio

class Estado(Enum):
    ROTO = "roto"
    LISTO = "listo"

class Gpu(Hardware):
    def __init__(self, fabricante, condicion, estado, color, precio, memoria, ventiladores, resolucion, vida):
        super().__init__(fabricante, condicion, estado, color, precio)
        self.memoria = memoria
        self.ventiladores = ventiladores
        self.resolucion = resolucion
        self.vida = vida
    
    def mostrar_gpu(self):
        print(f'Fabricante: {self.fabricante}')
        print(f'Condicion: {self.condicion}')
        print(f'Estado: {self.estado}')
        print(f'Color: {self.color}')
        print(f'Precio: {self.precio}')
        print(f'Memoria: {self.memoria}')
        print(f'Ventiladores: {self.ventiladores}')
        print(f'Resolucion: {self.resolucion}')
        print(f'Vida util: {self.vida}')
    
    def reparar(self):
        if self.estado == "roto":
            self.estado == "listo"
            print("arreglado")
        else:
            print("Esta listo para usarse, no necesita arreglarse")

    #con solo self, estamos usando los datos previamente instanciados en placa1
    def usar(self):
        while self.vida > 0:
            print(f'la placa se esta usando, le quedan {self.vida} usos')
            self.vida -= 1
        print("La placa ya no tiene vida, 'esta muerta'")

class Compania(Enum):
    CLARO = "CLARO"
    PERSONAL = "PERSONAL"
    MOVISTAR = "MOVISTAR"

class Sistema_operativo(Enum):
    ANDROID = "ANDROID"
    IOS = "IOS"

class Celular(Hardware):
    def __init__(self, fabricante, condicion, estado, color, precio, compania, sistema_operativo, pixeles, contactos):
        super().__init__(fabricante, condicion, estado, color, precio)
        self.compania = compania
        self.sistema_operativo = sistema_operativo
        self.pixeles = pixeles
        self.contactos = contactos

    def mostrar_celular(self):
        print(f'Fabricante: {self.fabricante}')
        print(f'Condicion: {self.condicion}')
        print(f'Estado: {self.estado}')
        print(f'Color: {self.color}')
        print(f'Precio: {self.precio}')
        print(f'Compania: {self.compania}')
        print(f'Sistema Operativo: {self.sistema_operativo}')
        print(f'Pixeles de la camara: {self.pixeles}')
        print(f'Lista de contactos: {self.contactos}')
    
    #para agregar numeros a nuestro diccionario de contactos, la funcion ademas del self debe recibir
    #2 parametros, nombre y numero
    def agregar_numero(self, nombre, numero):
        self.contactos[nombre] = numero
    
    def borrar_numero(self, nombre):
        del self.contactos[nombre]
        
placa1 = Gpu(Fabricante.NVIDIA.value, Condicion.USADO.value, Estado.LISTO.value, "Negro", 
             "$5000", "4 GB", 1, "1920x1080", 5)
#placa1.mostrar_gpu()
#placa1.reparar()
#placa1.usar()
#placa1.mostrar_gpu()

celular1 = Celular(Fabricante.SAMSUNG.value, Condicion.USADO.value, Estado.LISTO.value, "Plateado", 569000,
                   Compania.CLARO.value, Sistema_operativo.ANDROID.value, 50, {})

celular1.mostrar_celular()
celular1.agregar_numero("Albeto", 3517788999)
celular1.mostrar_celular()