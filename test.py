print("hola mundo")
c=0
r=0
while c < 101:
   r += c 
   c += 1
print("el resultado es: ",r)
lista1=["lunes","martes","miercoles","jueves","viernes"]
print(lista1)
print("El ultimo elemento es: ",lista1[4])
lista1[2]="sabado"
print("lista modificada: ",lista1)
lista1.extend(["sol","luna"])
print("lista modificada: ",lista1)
lista1.remove("lunes")
print("lista modificada: ",lista1)

def verificar_calificacion(c1,c2,c3):
   #c1=int(input("ingrese la primera nota: "))
   #c2=int(input("ingrese la segunda nota: "))
   #c3=int(input("ingrese la tercera nota: "))
   prom=(c1+c2+c3)//3
   if prom >= 6:
      return "aprobado"
   else:
      return "desaprobado"
condicion= verificar_calificacion (3,2,6)
print(condicion)
