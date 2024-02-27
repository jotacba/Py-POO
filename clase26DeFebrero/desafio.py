"""
Enunciado
Cierta empresa requiere una aplicación informática 
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo. 

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""
from enum import Enum

class Categoria(Enum):
    SALARIOFIJO = "Salario Fijo"
    COMISION = "Comision"

class Salario(Enum):
    MINIMO = 500000
    BASICO = 600000
class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso, categoria):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso
        self.categoria = categoria

    def mostrarEmpleado(self):
        pass

    def salarioFinal(self):
        pass

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, categoria, salarioMinimo, clientesCaptados, montoPorCliente):
        super().__init__(dni, nombre, apellido, anioIngreso, categoria)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente
    
    def mostrarEmpleado(self):
        print(f'Dni: {self.dni}')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Anio de Ingreso: {self.anioIngreso}')
        print(f'Categoria: {self.categoria}')
        print(f'Salario Minimo: {self.salarioMinimo}')
        print(f'Clientes Captados: {self.clientesCaptados}')
        print(f'Monto por Cliente: {self.montoPorCliente}')

    def salarioFinal(self):
        salarioFinal = self.clientesCaptados * self.montoPorCliente
        if salarioFinal < self.salarioMinimo:
            salarioFinal = self.salarioMinimo
        return salarioFinal
    
    

class Porcentaje(Enum):
    NADA = "NADA"
    CINCO = 5
    DIEZ = 10

class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, categoria, sueldoBasico, porcentajeAdicional, antiguedad):
        super().__init__(dni, nombre, apellido, anioIngreso, categoria)
        self.sueldoBasico = sueldoBasico
        self.porcentajeAdicional = porcentajeAdicional
        self.antiguedad = antiguedad

    def mostrarEmpleado(self):
        print(f'Dni: {self.dni}')
        print(f'Nombre: {self.nombre}')
        print(f'apellido: {self.apellido}')
        print(f'Anio de Ingreso: {self.anioIngreso}')
        print(f'Categoria: {self.categoria}')
        print(f'Sueldo Basico: {self.sueldoBasico}')
        print(f'Porcentaje Adicional: {self.porcentajeAdicional}')
        print(f'Antiguedad: {self.antiguedad}')

    def salarioFinal(self):
        sueldoFinal = self.sueldoBasico
        if self.antiguedad < 2:
            sueldoFinal = self.sueldoBasico
        elif self.antiguedad >= 2 and self.antiguedad <= 5:
            sueldoFinal = self.sueldoBasico * 1.05
        else:
            sueldoFinal = self.sueldoBasico * 1.1
        return sueldoFinal

empleados = [EmpleadoComision("30310031", "Facundo", "Colidio", 2023, Categoria.COMISION.value ,Salario.MINIMO.value, 3, 150000),
             EmpleadoComision("98976002", "Miguel", "Borja", 2022, Categoria.COMISION.value, Salario.MINIMO.value, 5, 110000),
             EmpleadoFijo("40123456", "Claudio", "Echeverri", 2023,  Categoria.SALARIOFIJO.value, Salario.BASICO.value, Porcentaje.CINCO.value, 3),
             EmpleadoFijo("30987654", "Santiago", "Simon", 2021, Categoria.SALARIOFIJO.value ,Salario.BASICO.value, Porcentaje.DIEZ.value, 7),
             EmpleadoFijo("30123456", "Rodrigo", "Villagra", 2023, Categoria.SALARIOFIJO.value, Salario.BASICO.value, Porcentaje.DIEZ.value, 8),
             EmpleadoComision("29097623", "Esequiel", "Barco", 2021, Categoria.COMISION.value, Salario.MINIMO.value, 2, 200000),
             EmpleadoFijo("38123456", "Agustin", "Sant'Anna", 2023, Categoria.SALARIOFIJO.value, Salario.BASICO.value, Porcentaje.CINCO.value, 1),
             EmpleadoComision("28765234", "Leandro", "Gonzales", 2020, Categoria.COMISION.value, Salario.MINIMO.value, 2, 300000),
             EmpleadoFijo("95912180", "Paulo", "Diaz", 2019, Categoria.SALARIOFIJO.value, Salario.BASICO.value, Porcentaje.DIEZ.value, 10),
             EmpleadoComision("25310180", "Enzo", "Diaz", 2022, Categoria.COMISION.value, Salario.MINIMO.value, 4, 200000),
             EmpleadoComision("20986745", "Franco", "Armani", 2018, Categoria.COMISION.value, Salario.MINIMO.value, 6, 100001)]


def mostrarSalarios(empleados):
    for empleado in empleados:
        print(f'El empleado: {empleado.nombre} {empleado.apellido}, gana ${empleado.salarioFinal()}')

#ahora creamos una funcion que reciba una lista de empleados, mas concretamente de objetos empleados
#(lista de objetos y no lista de listas). creamos la variable max_clientes_anterior que guarda la cantidad
#de clientes en cada iteracion, la primera vez sera mayor porque vale 0 (empleado.clientesCaptado
# > max_clientes_anterior). la nueva variable se guarda en max_clientes_actual y de paso guardamos el 
#nombre del empleado para usarlo despues. De esta manera en cada iteracion se compara si la
#cantidad de clientes es mayor que el valor guardado en max_clientes_anterior y de ser asi se guarda
#en max_clientes_actual.
#como solo buscamos empleados por comision se agrega un atributo a cada objeto que nos indique si lo es
#(Categoria.COMISION.value)
def empleadoConMasClientes(empleados):
    max_clientes_anterior = 0
    max_clientes_actual = 0
    nombre_empleado = ""
    for empleado in empleados:
        if empleado.categoria == Categoria.COMISION.value:
            #max_clientes_anterior = 0
            if empleado.clientesCaptados > max_clientes_anterior: 
                max_clientes_anterior = empleado.clientesCaptados
                max_clientes_actual = max_clientes_anterior
                nombre_empleado = empleado.nombre + " " + empleado.apellido
                
            #print(empleado.clientesCaptados)

    print(f'El empleado con la mayor cantidad de clientes es: {nombre_empleado}')

mostrarSalarios(empleados)
empleadoConMasClientes(empleados)