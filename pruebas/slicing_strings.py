cadena = "joelinho"
#print(cadena[0])
#cadena[1] = "a"
#al ejecutar obtenemos un error, ya que los "str" son inmutables
#usaremos la funcion slicing que permite obtener cortes, rebanadas de strings y tambien de listas, tuplas.

#La sintaxis es cadena[inicio:fin:paso]
#inicio: si queremos empexar desde el inicio ponemos 0
#fin: hasta que caracter queremos cortar
#paso: tamaño del salto que queremos hacer entre caracteres
#entonces para poder cambiar la "o" en posicion 1 lo haremos asi
print(cadena[0:3])
print(cadena[0:1])
print(cadena[2:])
#para cambiar joelinho a jaelinho
print(f'{cadena[0:1]}a{cadena[2:]}')
nueva_cadena = cadena[0:1]+"a"+cadena[2:]
print(nueva_cadena)
