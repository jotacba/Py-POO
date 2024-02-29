'''Una fábrica de instrumentos musicales posee una lista con todas sus sucursales.
Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta.
De cada uno de ellos se sabe su ID alfanumérico, su precio y su tipo
(Percusión, Viento o Cuerda).

Puntos a desarrollar
1)Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten
las clases con sus atributos, métodos y relaciones (los constructores pueden omitirse).

2) Crear un proyecto en Python que resuelva:
    A) método listarInstrumentos que muestre en la consola todos los
    datos de cada uno de los instrumentos. - DEVOLVEME TODOS LOS INSTRUMENTOS
    B) método instrumentosPorTipo que devuelva una lista de 
    instrumentos cuyo tipo coincida con el recibido por parámetro. ... DE CUERDAS (FILTRO)
    C) método borrarInstrumento que reciba un ID y elimine el
    instrumento asociado a tal ID de la sucursal donde se encuentre.
    D) método porcInstrumentosPorTipo que reciba el nombre de una
    sucursal y retorne los porcentajes de instrumentos por tipo que hay para tal sucursal.'''

from enum import Enum

class TipoInstrumento(Enum):
    PERCUSION = "Percusion"
    VIENTO = "Viento"
    CUERDA = "Cuerda"

class Fabrica:
    def __init__(self):
        self.sucursales = []

    def agregarSucursal(self, sucursal):
        self.sucursales.append(sucursal)

    #Como la lista sucursales tiene nombre y una lista con instrumentos, es necesario iterar sobre
    # sucursal.instrumentos 
    def listarInstrumentos(self, sucursales):
        for sucursal in sucursales:
            for instrumento in sucursal.instrumentos:
                print("******************************")
                print(f'ID: {instrumento.id}')
                print(f'Precio: {instrumento.precio}')
                print(f'Tipo de instrumento: {instrumento.tipoInstrumento}')
                print("******************************")
    
    def instrumentoPorTipo(self, sucursales, tipo):
        lista = []
        for sucursal in sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipoInstrumento == tipo:
                    lista.append(instrumento)
        print("**************************************")
        print(f'Los instrumentos de tipo {tipo.value} son:') 
        for elemento in lista:
           print(elemento.id)
        print("**************************************")

    def borrarInstrumento(self, id):
        for sucursal in fabrica.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.id == id:
                    sucursal.instrumentos.remove(instrumento)
                    print(f'Se elimino el instrumento {instrumento.id} de la sucursal {sucursal.nombre}')
                    break
        #tambien podriamos mostrar la lista de todos los instrumentos y comprobar que ya no esta el del id
        #que se ingreso como parametro.
        #fabrica.listarInstrumentos(fabrica.sucursales)
        
    def porInstrumentosPorTipo(self, nombreSucursal):
        for sucursal in fabrica.sucursales:
            if sucursal.nombre == nombreSucursal:
                cantidad = len(sucursal.instrumentos)
                c1 = 0
                v1 = 0
                p1 = 0
                for instrumento in sucursal.instrumentos:
                    if instrumento.tipoInstrumento == TipoInstrumento.CUERDA:
                        c1 += 1
                    elif instrumento.tipoInstrumento == TipoInstrumento.VIENTO:
                        v1 += 1
                    else:
                        p1 += 1
        if cantidad != 0:
            pc = round((c1 * 100 / cantidad), 2)
            pv = round((v1 * 100 / cantidad), 2)    
            pp = round((p1 * 100 / cantidad), 2)
        print(f'El porcentaje de instrumentos de cuerda es: {pc}')
        print(f'El porcentaje de instrumentos de viento es: {pv}')
        print(f'El porcentaje de instrumentos de percusion es: {pp}')
        
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    """def listarInstrumentos(self, instrumentos):
        for instrumento in instrumentos:
            print(f'ID: {instrumento.id}')
            print(f'Precio: {instrumento.precio}')
            print(f'Tipo de Instrumento: {instrumento.tipoInstrumento}')"""
    
class Instrumento:
    def __init__(self, id, precio, tipoInstrumento):
        self.id = id
        self.precio = precio
        self.tipoInstrumento = tipoInstrumento
    
fabrica = Fabrica()
sucursal1 = Sucursal("Sucursal 1")
sucursal2 = Sucursal("Sucursal 2")
sucursal3 = Sucursal("Sucursal 3")
instrumento1 = Instrumento("1a", 45000, TipoInstrumento.CUERDA)
instrumento2 = Instrumento("1b", 55000, TipoInstrumento.CUERDA)
instrumento3 = Instrumento("1c", 65000, TipoInstrumento.CUERDA)
instrumento4 = Instrumento("1d", 75000, TipoInstrumento.VIENTO)
instrumento5 = Instrumento("1e", 85000, TipoInstrumento.PERCUSION)
instrumento6 = Instrumento("2a", 41000, TipoInstrumento.VIENTO)
instrumento7 = Instrumento("2b", 51000, TipoInstrumento.VIENTO)
instrumento8 = Instrumento("2c", 61000, TipoInstrumento.VIENTO)
instrumento9 = Instrumento("2d", 71000, TipoInstrumento.CUERDA)
instrumento10 = Instrumento("2e", 81000, TipoInstrumento.PERCUSION)
instrumento11 = Instrumento("3a", 100000, TipoInstrumento.PERCUSION)
instrumento12 = Instrumento("3b", 200000, TipoInstrumento.PERCUSION)
instrumento13 = Instrumento("3c", 300000, TipoInstrumento.PERCUSION)
instrumento14 = Instrumento("3d", 400000, TipoInstrumento.CUERDA)
instrumento15 = Instrumento("3e", 500000, TipoInstrumento.VIENTO)

fabrica.agregarSucursal(sucursal1)
fabrica.agregarSucursal(sucursal2)
fabrica.agregarSucursal(sucursal3)

sucursal1.agregarInstrumento(instrumento1)
sucursal1.agregarInstrumento(instrumento2)
sucursal1.agregarInstrumento(instrumento3)
sucursal1.agregarInstrumento(instrumento4)
sucursal1.agregarInstrumento(instrumento5)
sucursal2.agregarInstrumento(instrumento6)
sucursal2.agregarInstrumento(instrumento7)
sucursal2.agregarInstrumento(instrumento8)
sucursal2.agregarInstrumento(instrumento9)
sucursal2.agregarInstrumento(instrumento10)
sucursal3.agregarInstrumento(instrumento11)
sucursal3.agregarInstrumento(instrumento12)
sucursal3.agregarInstrumento(instrumento13)
sucursal3.agregarInstrumento(instrumento14)
sucursal3.agregarInstrumento(instrumento15)

fabrica.listarInstrumentos(fabrica.sucursales)
fabrica.instrumentoPorTipo(fabrica.sucursales, TipoInstrumento.CUERDA)
fabrica.borrarInstrumento("1b")
fabrica.porInstrumentosPorTipo("Sucursal 2")