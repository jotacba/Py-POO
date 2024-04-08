'''Consigna:
Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos 
por la terminal acorde a distintas opciones.  Para ellos debemos definir una función que reciba parámetros:
Combinar funciones nativas y funciones definidas,
condicionales, y bucles.
Si el usuario ingresa el nro 1, realiza la acción A.
Si el usuario ingresa el nro 2, realiza la acción B.'''

print("Si el numero ingresado es par, obtener su raiz cuadrada,si es impar, sumar todos los numeros desde cero hasta el mismo numero")
#numero=int(input("Ingrese un numero: "))
def miFuncion(numero):
    if numero%2 == 0:
        resultado=pow(numero, 0.5)
    else:
        contador = 0
        resultado  = 0
        while contador <= numero:
            resultado = resultado + contador
            contador += 1
    return resultado
print(miFuncion(5))