# from re import A


# tupla = (1,2,3,4,5,"a","b")
# tupla1 = ()#vacia
# tupla2 = (1,2,3,4,5,6,7,8,(1,2,3,4))
# tupla3 = (tupla, tupla2)

# #print(tupla, tupla2, tupla3)
# #print (tupla3[1][8][2],tupla3[1][6])

# #operadores
# #+ concatenar tuplas
# tupla4=(tupla+tupla3) #juntar
# #print (tupla4)

# #* repite

# tupla5 = tupla*3
# #print (tupla5)

# #Comparar < > >= <= == !=
# #print(("lunes",123)<("martes", 123))

# #posiciones

# tupla5=("Lunes",123)
# tupla6=("lunes",124)

# #Posiciones
# cantidad=len(tupla5)
# #print(tupla5[cantidad-1])
# #print(tupla5[-1])


# #condicionales
# #semana=("lunes","martes","miercoles","jueves","viernes")
# #busqueda=input()
# #for i in range(0,len(semana)):
#   #if busqueda not in semana: #no se encuentra
#     #print("No se encuentra")
#   #else:
#     #print("Si se encuentra")
#     #print(i)
#     #break
# #contador=0
# #for j in semana:
#   #if busqueda in semana:
#     #print(contador)
#     #break
#   #else:
#     #print("no esta")
#   #contador+=1

#   #asignacion multiple
# tupla7=(1,2,3,4)
# a,b,c,d=tupla7
# print (a,b,c,d)
# a,b=b,a
# print(a,b,c,d,tupla7)
# #primero variables = (instruccion ciclo)
# var1,var2=(tupla7[i] for i in(1,3))
# print (var1,var2)

# #organizacion descendentemente 2(min and max)

# num1 = int(input("n1"))
# num2 = int(input("n2"))
# print(num1,num2)

# #organizar descendentemente 2(minimo y el maximo) funcion
# def minmax(n1,n2):
#   if n1>n2:
#     return n1,n2
#   else:
#     return n2,n1

# num1=int(input("n1"))
# num2=int(input("n2"))
# max,min=minmax(num1,num2)
# print(max,min)

# #Metodos asociados a las tuplas
# semana=("lunes","martes","miercoles","jueves","viernes")
# print(len(semana))#cantidad de elementos de la tupla
# #subtuplas rangos [valor inicial:valor final:incremento]
# print(semana[1:4])
# print(semana[::-1])
# print(semana[:2])
# print(semana[3:3])
# #count contar la cantidad de veces que esta un elemento
# numeros=(1,2,3,4,5,6,4,3,2,1,8,9,5,4,5,6)
# print(numeros.count(5))
# print(numeros.count(10))
# #index metodo darnos la primera posicion(ocurrencia) de un valor
# print("Primera aparición",numeros.index(4))
# for i in range(0,len(numeros)):
#   if(numeros[i]==4):
#     print(i)
# #min, max funcion
# #t=(4,5,-1,6,7)
# #print(max(t))
# #print(min(t))

#cadena-tupla tuple (manejarle el tipo de dato) casting
#los cambios no son permitidos, incluyendo reemplazar datos
# dia="lunes"
# tupla=tuple(dia)
# print(tupla)


#cree una tupla con los meses de año, pida un valor(hasta que ingrese el que es) al usuario si esta entre los elementos
#de la tupla imprima el contenido sino imprima un mensaje de error
# meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
# bandera=True
# while bandera:
#     valor=int(input("Ingrese un valor:"))
#     if valor>0 and valor<=len(meses):
#         print(meses[valor-1])
#         bandera=False
#     else:
#         print("ingrese otro valor")

#tuple map(tipo de datos(casting),input())

# deli=input()
# numeros=tuple(map(int,input("Valores: ").split(deli)))
# print(numeros)

# #listas(Array) [, , , ,] mutables(cambiar su tamaño) heterogeneos u homogeneos..identificador=[lista]
# lista=[] #vacia
# lista1=[1,2,3,4,5,6] #homogenea
# print(lista1[10])
# lista2=["a","b",["c","d"],1,2,3] #heterogenea #posiciones 0-cantidad-1
# print(lista2[2])
# lista3=[lista1,lista2] #listas anidadas
# print(lista3)
# print(lista3[1][2][0])
# print(lista1[0])
# #Operadores
# #+Concatenar o juntar
# lista4=lista1+lista2
# print(lista4)
# print(lista4[11])
# #metodo juntar una lista con otra extend(agregar al final) listaextendida.metodo(listafinal)
# lista1.extend(lista2)
# lista1.extend(lista4)
# print(lista1)
# print(lista1[10])
# #Repetir *
# lista5=lista2*3
# print(lista5)
# #Operadores Relacionales > < >= <= == !=
# print(["martes",10]>["miercoles",11])
# print(["miercoles",10]<["miercoles",11])
# print(["azul",345,456]!=["azul","345","456"])
# #Subindice
# print(lista5[-4])
# print(lista5[::-1])

#condicionales
# numeros=[10,20,30,40,50,60,70,80,90,100]
# busqueda=int(input("ingrese numero buscado"))
# if busqueda in numeros: #if busqueda not in numeros
#   print("Si esta")
# else:
#   print("No esta")

# #ciclos (iteracion, relleno(creacion de la lista) de las listas)
# for i in numeros:
#   print(i, end=" ")

# for j in range(0,len(numeros)):
#   print(numeros[j], end=" ")

# #ingresados por el usuario
# ingreso=[]
# cantidad=int(input("cantidad"))
# for i in range(0,cantidad):
#   valor=int(input("valor"))
#   #append(agregar valor al final de la lista)
#   ingreso.append(valor)
# print(ingreso)

# #ingreso valores a una lista con valor inicial
# #nombre de la lista=[instruccion(operaciones) ciclo rango]
# ingreso1=[2**j for j in range(2,6)] #=asignacion ingreso[j]=2**j
# print(ingreso1)

# #asignaciones multiple
# multiple=[4,5,6]
# n1,n2,n3=multiple
# print(n1,n2,n3)#asignacion de la lista
# ciclo=[1,2,3,4,5,6,7,8,9,10] #ciclo [instruccion(lista[posicion]) ciclo (posiciones)]
# p1,p2=[ciclo[k] for k in(4,8)]
# print(p1,p2)
# r1,r2,r3,r4,r5=[ciclo[h] for h in range(0,10,2)]
# print(r1,r2,r3,r4,r5)

#descendente 3 valores
# def descendente(n1,n2,n3):
#   if n1>n2 and n1>n3:
#     mayor=n1
#     if n2>n3:
#       medio=n2
#       peque=n3
#     else:
#       medio=n3
#       peque=n2
#   elif n2>n3 and n2>n1:
#     mayor=n2
#     if n3>n1:
#       medio=n3
#       peque=n1
#     else:
#       medio=n1
#       peque=n3
#   else:
#     mayor=n3
#     if n2>n1:
#       medio=n2
#       peque=n1
#     else:
#       medio=n1
#       peque=n2
#   return mayor,medio,peque

# v1=int(input("Valor 1: "))
# v2=int(input("Valor 2: "))
# v3=int(input("Valor 3: "))
# may,med,pe= descendente(v1,v2,v3)
# print("el Mayor",may, "el Medio",med, "El peque",pe)

#metodos y funciones
# numerostodos=[1,2,3,4,5,6,7,8,9,10]
# #len: cantidad de elementos de la lista
# print("Elementos",len(numerostodos))
# #cambiar elementos de una lista
# numerostodos[5]=11
# numerostodos[9]=22
# numerostodos[3]=15
# numerostodos[-2]=32
# print(numerostodos)
# #Agregar elementos o insertar append(agregar al final) insert(posicion,valor)
# numerostodos.insert(0,34)
# numerostodos.insert(6,"a")
# numerostodos.insert(7,22)
# print(numerostodos)
# #eliminar (remove) primera aparicion del elemento clear(todo) pop(posicion)
# numerostodos.remove(22)
# print(numerostodos)
# borrado=numerostodos.pop(11)
# print(borrado)
# print(numerostodos)

# #reto3 
# impresion=[1,2,3,4,5]
# for i in impresion:
#   print(i, end=" ")

#reto 3 convertir a lista
# lista=list(map(int,input().split(",")))
# print(lista)

#Metodos o funciones
# multiplos=[10,20,60,40,50,60,70,90,90]
# #Sublistas [valor inicial:valorfinal-1:incremento]
# print(multiplos[:5])
# print(multiplos[1:7])
# print(multiplos[::-1])
# print(multiplos[5:5])
# print(multiplos[5:12])
# #count: contar la cantidad de veces que se repite un valor
# print(multiplos.count(60))
# #index encontrar la primera ocurrencia del valor
# print(multiplos.index(60))
# #max y min lista
# print(max(multiplos))
# print(min(multiplos))
# #Ordenar : organizarla menor a mayor o de mayor a menor sort sobre la misma lista
# multiplos.sort()
# print(multiplos)
# multiplos.sort(reverse=True)
# print(multiplos)

#cadena en una lista(list)
cadena="Hoy es miercoles"
listaconver=list(cadena)
print(listaconver)
tupla=(1,2,3,4)
listaconver1=list(tupla)
print(listaconver1)