    #Creamos 2 listas
diasSemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
diasFestivos = ["san valentin", "dia del amigo", "feriado"]

    #acceder individualmente
print(f'El primer dia de la semana es {diasSemana[0]}')

    #modificamos un elemento de una lista
print(f'la lista sin modificar es {diasFestivos}')
diasFestivos[0] = "dia de los enamorados"
print(f'la lista modificada es {diasFestivos}')

    #agregamos un elemento al final de una lista
diasFestivos.append("carnaval")
print(f'los nuevos dias festivos son: {diasFestivos}')

    #añadir una lista a otra preexistente
diasSemana.extend(diasFestivos)
print(f'la nueva lista unificada es: {diasSemana}')

    #agregar elementos en un index o posicion especifica
    #tiene 2 parametros, el primero es la posicion y el segundo es el elemento a agregar
diasSemana.insert(0, "feriadoxd")
print(f'la nueva lista con el elemento que se inserto es: {diasSemana}')

    #eliminar el ultimo elemento
diasSemana.pop()
print(f'si eliminamos el ultimo elemento {diasSemana}')

    #tambien podemos eliminar un elemento especifico
diasSemana.pop(0)
print(f'la lista con el elemento inicial eliminado es: {diasSemana}')

    #eliminar un elemento mediante su nombre especifico
diasSemana.remove("dia de los enamorados")
print(f'eliminamos el elemento "dia de los enamorados" de la lista {diasSemana}')

    #Ciclo for
diasSemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for dia in diasSemana:
    print(f'dia: {dia}')

    #ordenamiento de elementos de una lista
    #numeros

listaNumeros = [5, 3, 6, 98, 73, 100, 2, 664]
print(f'lista denumeros: {listaNumeros}')
listaNumeros.sort()
print(f'lista de numeros ordenada en orden ascendente: {listaNumeros}')
listaNumeros = [5, 3, 6, 98, 73, 100, 2, 664]
    
    #la funcion reverse solo invierte el orden posicional pero no ordena
listaNumeros.reverse()
print(f'lista de numeros invertida pero no ordenada: {listaNumeros}')
listaNumeros = [5, 3, 6, 98, 73, 100, 2, 664]

    #si queremos ordenarla en orden descendente debemos usar sort primero y reverse despues
listaNumeros.sort()
listaNumeros.reverse()
print(f'lista de numeros en orden descendente: {listaNumeros}')

    #Tuplas: recordemos que son estructuras de datos inmutables
puntosCardinales = ("norte", "sur", "este", "oeste")
print(f'la tupla de puntos cardinales es: {puntosCardinales}')
for p in puntosCardinales:
    print(f'{p}')

    #la funcion count cuenta cuantos elementos especificados hay en la tupla
print(puntosCardinales.count("este"))

    #la funcion index indica la posicion del elemento indicado
print(puntosCardinales.index("sur"))

    #Diccionarios: key - value
persona = {"nombre" : "joel",
           "apellido" : "ramos",
           "edad" : 31,
           "sexo" : "varon",
           "altura" : 1.70,
           "notas" : [9, 10, 9, 8, 8],
           "esAlumno" : True}
print(f'mi diccionario de datos personales es: {persona}')
print(f'mi nombre es: {persona["nombre"]}')

    #con la funcion get obtenemos el valor de una llave
name = persona.get("nombre")
print(f'mi nombre almacenado en una variable: {name}')

    #se pueden usar las mismas funciones que las listas 
persona["apellido"] = "delgado"
print(f'modifique mi apellido: {persona}')

    #mostrando solo las keys
print(f'solo las llaves: {persona.keys()}')

    #mostrando solo los values
print(f'solo los valores: {persona.values()}')

    #el metodo items devuelve una lista con las keys y values del diccionario
print(persona.items())

    #podemos convertirlo a lista
print(list(persona.items()))

print(persona)

    #Funciones
    #declarar y definir una funcion
def sumar_iva(precioInicial):
    precio_con_iva = precioInicial * 1.21
    return precio_con_iva
print(f'calcular el precio : {sumar_iva(900)}')

def bienvenida(nombre, club, mensaje):
    print(f'Hola {nombre}, bienvenido al club {club}, {mensaje}')

print(bienvenida("joel", "River Plate", "ahora puede conocer el monumental"))
bienvenida("beto", "belgrano", "el sabado ganan el clasico")