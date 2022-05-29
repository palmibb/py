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
# cadena="Hoy es miercoles"
# listaconver=list(cadena)
# print(listaconver)
# tupla=(1,2,3,4)
# listaconver1=list(tupla)
# print(listaconver1)

#Realizar un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura termina
#cuando se introduzca como nombre un * al finalizar se entregaran los siguientes datos:
#Los alumnos mayores de edad y el alumno mas viejito y joven de todos
# nombres=[]
# edades=[]
# while True:
#   nombre=input("ingrese el nombre")
#   if nombre=="*":
#     break
#   else:
#     nombres.append(nombre)
#     edades.append(int(input("Ingrese la edad")))

# max_edad=max(edades)
# min_edad=min(edades)
# for i in range(0,len(edades)):
#   if edades[i]>=18:
#     print("Es mayor de edad",nombres[i],edades[i])
#   if max_edad==edades[i]:
#     print("El mas viejito es",nombres[i])
#   if min_edad==edades[i]:
#     print("El mas joves es:",nombres[i])

# for i,j in zip(nombres,edades): #for iteracion en paralelo
#   if j>=18:
#     print(i,j)
#   if max_edad==j:
#     print("El mas viejito es",i)
#   if min_edad==j:
#     print("El mas joves es:",i)

# arreglos vectores(unidimensional(tupla o una lista(si o si homogeneos))) - homogeneos quiere decir mismo tipo de datos - componentes(valores)
#cuando es una lista el tamaño varia - arreglos con numpy(inmutables) no puede cambiar el tamaño
# arreglo=[] #vacio
# arreglo1=[1,2,3,4,5,6] #6 componentes int posicion 0-cantidad de componentes -1
# arreglo2=[True,False,False,True]
# arreglo3=[6.1,6.2,6.3] #3 componentes

# #lectura de un arreglo
# #[instruccion ciclo instruccion de ingreso de datos] tipo de dato de mi arreglo
# def leerarregloentero():
#   return [int(valor) for valor in input("Ingrese arreglo").split(" ")]

# #print(leerarregloentero())

# def leerarregloflotantes():
#   return [float(valor) for valor in input("Ingrese arreglo").split(" ")]

# print(leerarregloflotantes())

# #sumar los componentes de un arreglo
# def suma_arreglo(A):
#   suma=0
#   for i in A:
#     suma=suma+i
#   return suma

# #maximo de un arreglo
# def max_arreglo(A):
#   maximo=0
#   for j in range(0,len(A)):
#     if maximo<A[j]: #if A[maximo]<A[j]: maximo=j
#       maximo=A[j]
#   return maximo

# print("La suma de los componentes del arreglo es:",suma_arreglo([1,2,3,4,5,6]))
# print("El valor maximo es:",max_arreglo([1,2,3,4,5,6]))

# #libreria con Numpy: inmutables que no se puede cambiar su tamaño
# import numpy as np #sobrellame 
# lista=[1,2,3,4,5]
# vector=np.array(lista) #creacion
# print(vector)
# vector=np.array([]) #no podre ingresarle mas valores
# #vector.append(valor)
# #rellenan de ceros o de unos
# cantidad=int(input())
# vector1=np.zeros(cantidad)
# vector2=np.ones(cantidad)
# print(vector1)
# print(vector2)
# vector1[2]=4
# print(vector1)
# #Llenarlo
# for i in range(0,cantidad):
#   x=int(input("ingrese el valor"))
#   vector1[i]=x
# print(vector1)

# import numpy as np
# vector2=np.array([9,8,7,6,5])
# vector3=np.array([1,2,3,4,5])
# #Operaciones
# print(vector2+1)
# print(vector2*5)
# print(np.sum(vector2))
# print(np.mean(vector2))
# print(vector2+vector2)
# print(vector2+vector3)
# #size(tamaño de el arreglo cantidad de componentes de ese arreglo)
# #print(len(vector2))
# print(np.size(vector2)) #cantidad de componentes de ese arreglo
# #ndim: la cantidad de dimensiones
# #dtype tipo de dato de el array #se usa en un comparacion int32(tipo escalar) o float64, U16 memoria
# print(np.ndim(vector2))

# #Matriz: listas de una mas de una dimension (filas,columnas)
# #listas anidadas
# matriz=[[1,2,3],[4,5,6],[7,8,9]] #3,3
# #print(len(matriz))
# matriz1=[[1,2],[3,4],[4,6]] #3,2
# print(matriz[2][1])
# for i in range(0,len(matriz)):
#   for j in range(0,len(matriz[i])):
#     print(matriz[i][j])


# #Construir una matriz
# filas=int(input("Filas"))
# columnas=int(input("Columnas"))
# creada=[]
# for i in range(0,filas):
#   temporal=[]
#   for j in range(0,columnas):
#     elemento=int(input("ingrese el elemento"))
#     temporal.append(elemento)
#   creada.append(temporal)
# print(creada)

# #una funcion que permita construir una nueva matriz con los cuadrados de una matriz dada
# def cuadrados(M):
#   R=[]
#   for k in range(0,len(M)):
#     temporal=[]
#     for h in range(0,len(M[k])):
#       cuadrado=M[k][h]*M[k][h]
#       temporal.append(cuadrado)
#     R.append(temporal)
#   return R #siempre en mayuscula
# print(cuadrados([[1,2,3],[4,5,6]]))


# #Diagonal de una matriz (cuadrada)
# f=int(input())
# c=int(input())
# diagonal=[]
# for filas in range(0,f):
#   temporal=[]
#   for columnas in range(0,c):
#     num=float(input())
#     temporal.append(num)
#   diagonal.append(temporal)
# print(diagonal)
# for g in range(0,f):
#   print(diagonal[g][g])

# #Ejercicio 1 Pag 29
# arreglo=[float(valor) for valor in input("Ingrese el valor").split(" ")]
# suma=0
# for i in range(0,len(arreglo)):
#   suma=suma+arreglo[i]
# promedio=suma/len(arreglo)
# print(arreglo)
# print("El promedio es:",promedio)

# #Ejercicio 2 Pg 29
# arreglo=[int(valor) for valor in input("Ingrese el valor").split(" ")]
# arreglo1=[int(valor) for valor in input("Ingrese el valor").split(" ")]
# producto=0
# vector=[]
# for j in range(0,len(arreglo1)):
#   producto=producto+arreglo[j]*arreglo1[j]
#   vector.append(arreglo[j]*arreglo1[j])
# print(producto)
# print(vector)

# matriz1=[[1.3,2.4,3.5],[9.2,4.5,6.7]]
# matriz2=[[10,11,12],[13,14,15]]
# matriz3=[]
# suma=0
# for i in range(0,len(matriz1)):
#   temporal=[]
#   for j in range(0,len(matriz1[i])):
#     suma=matriz1[i][j]+matriz2[i][j]
#     temporal.append(suma)
#   matriz3.append(temporal)
# print(matriz3)
# #sumac=0
# # columna=int(input("cual columna"))
# # for t in range(0,len(matriz1)):
# #   sumac=sumac+matriz1[t][columna]
# # print(sumac) ctrl+}
# sumaf=0
# fila=int(input("cual fila"))
# for t in range(0,len(matriz1)):
#   sumaf=sumaf+matriz1[fila][t]
# print(sumaf)

# #Diccionarios: coleccion para manejar datos complejos mutable etiqueta(clave o llave) valor
# #clave(unicas):valor(todo tipo). 
# #parejas: clave(unicas(cadenas,numeros, no listas de listas,tuplas)) no puede ser cambiada
# #valor: tipo de dato, pueden ser cambiados no tienen que ser unicos. 
# #son colecciones desordenadas diccionario{clave:valor,clave:valor,clave:valor}
# #acceder a un valor siempre es con la clave
# persona={"nombre":["Alejandra","pedro"],"edad":30,"RH":"O-","telefono":3176821696}
# puertos={22:"SSH",80:"http",53:"DNS"}
# diccionario={}
# print(persona)
# #Acceder
# print(persona["nombre"][1],persona["edad"]) #clave
# #Operaciones
# #unir diccionarios(update) diccionario que sera ampliado.metodo(diccionario incorporado)
# persona.update(puertos)
# print(persona)
# puertos.update(persona)
# print(puertos)
# #comparar == != solamente la cantidad de item(clave:valor) que tenga el diccionario
# print({"dia":"lunes","anterior":"domingo"}=={"dia":2,"anterior":1}) #cantidad de elementos
# print({123:"rosas",83:"rojas"}=={123:"rojas",83:"rosas"})
# print({"Rotas":12}!={"rotas":12})
# #Agregar/modificar (clave estaa: cambia el valor, no esta:la agrega)
# persona["edad"]=56
# print(persona)
# persona[110]="POP"
# print(persona)
# persona[443]="https"
# print(persona)
# #eliminar referenciar la clave del 
# del persona[110]
# print(persona) 
# del persona["nombre"]
# print(persona)

#condicionales, ciclos
# diccionario1={'edad': 56, 'RH': 'O-', 'telefono': 3176821696, 22: 'SSH', 80: 'http', 53: 'DNS', 443: 'https'}
# buscando=input("Ingrese el valor buscado")
# verdad=buscando.isnumeric()
# if verdad==True:
#   buscando=int(buscando)
# if buscando in diccionario1: #not in
#   print("Si esta",diccionario1[buscando])
# else:
#   print("No esta")
# #ciclos
# for i in diccionario1:
#   print(i) #arroja las claves

# #claves y el valor
# for cl,val in diccionario1.items():
#   print(cl,":",val)

#Metodos
# diccionario2={'edad': 56, 'RH': 'O-', 'telefono': 3176821696, 22: 'SSH', 80: 'http', 53: 'DNS', 443: 'https'}
# puerto={22: 'SSH', 80: 'http', 53: 'DNS', 443: 'https'}
# #len=cantidad de items
# print(len(diccionario2))
# #obtener valor
# print(diccionario2["edad"])
# #get(verdad) get(verdad,falsedad)
# print(diccionario2.get("edad"))
# print(diccionario2.get(110,"clave no encontrada"))
# #max o min (claves)
# print(max(puerto))
# print(min(puerto))
# #obtener valores diccionario.values

# print(list(diccionario2.values()))
# print(list(puerto.keys()))

#llenando un diccianario
# diccionario0={}
# cantidad=int(input("Ingrese al Cantidad de Items: "))
# for i in range(0,cantidad):
#   clave=int(input("Ingrese la Clave: "))
#   valor=input("Ingrese el Valor: ")
#   diccionario0[clave]=valor
# print(diccionario0)

# diccionario3={}
# while True:
#   condicion=int(input("Ingrese 1 si desea parar: "))
#   if condicion == 1:
#     break
#   else:
#     clave=int(input("Ingrese la Clave: "))
#     valor=input("Ingrese el Valor: ")
#     diccionario3[clave]=valor

#solo se convierte listas de listas(matrices) o listas de tuplas a diccionarios dict
# dias=[[1,"lunes"],[2,"martes"],[3,"miercoles"],[4,"jueves"],[5,"viernes"]]
# dicciodias=dict(dias)
# print(dicciodias)
# dias1=[(1,"lunes"),(2,"martes"),(3,"miercoles"),(4,"jueves"),(5,"viernes")]
# print(dict(dias1))
# #copiar diccionario copy
# copia=dicciodias.copy()
# print("copia",copia)
# #dejarlo vacio
# dicciodias.clear()
# print(dicciodias)

# #EJERCICIO 1 Diccionarios
# import operator
# #sorted(ordenar un diccionario) claves
# num={1:10,2:9,3:8,4:6,13:2,11:23}
# letras={"e":1,"c":11,"b":10,"d":5,"a":6}
# print(sorted(letras.items()))
# print(sorted(num.items()))
# #valores libreria operator
# #itemgetter=valor(1 valor)(0 clave)
# print(sorted(letras.items(),key=operator.itemgetter(0)))
# print(sorted(num.items(),key=operator.itemgetter(1),reverse=True))

# ////

# #Ejercicio 2 Diccionario
# num={"e":1,"c":11}
# letras={"e":1,"c":11,"b":10,"d":5,"a":6}
# contar=0
# for clave,valor in num.items():
#   if clave in letras:
#     if valor==letras[clave]:
#       contar+=1
# if contar==len(num):
#   print("los items estan todos")
# else:
#   print("items no estan todos")

# ///



# #memoria: almacenamos los datos(valor o programas) a ejecutar una tarea en especifico
# #archivo: una unidad logica(bytes almacenados)que permite almacenar esos dato(memoria principal)
# #inicio y siempre tienen un fin. tamaño(peso)(bytes)
# #archivos de texto(ASCII(byte) planos .txt .html .py .c .java .csv)- 
# #binarios(conjunto de bytes .jpg .png .jpeg .gif .rar .pdf .doc)
# #operaciones: crear, abrir,cerrar, eliminar 
# #modo de apertura: with open(ruta del archivo,accion) as nombre del archivo(referencia en el codigo)
# #leer 'r' read escribir 'w' write
# with open('files/data.txt','r') as archivo:
#   dato=archivo.read()
#   print(dato)

# with open('files/escribir.txt','w') as escritura:
#   datos="hoy es martes 17 de mayo\n"
#   escritura.write(datos)
#   escritura.write(datos)
#   escritura.write(datos)
#   escritura.write(datos)
#   escritura.write(datos)

# with open('files/escribir.txt','r') as leer:
#   lectura=leer.read()
#   print(lectura)

# with open('files/data2.txt','a') as x:#a agregar al final append
#   data="Esto queda al final\n"
#   x.write(data)

# with open('files/data2.txt','a') as x1:#a agregar al final append
#   data1="Esto es el final final\n"
#   x1.write(data1)

# with open('files/data2.txt','r') as leer1: 
#   lectura1=leer1.read()
#   print(lectura1)

# #'r+': leer y escribir 'a+'escribir al final y leer

# #leer con tildes utf-8
# with open('files/data1.txt','r',encoding="utf-8") as leer2: 
#   print(leer2.read())

# with open('files/data1.txt','r',encoding="utf-8") as leer3: 
#   linea1=leer3.read(6)
#   linea2=leer3.read(10)
#   linea3=leer3.read(15)

# print(linea1)
# print(linea2)
# print(linea3)

#leer por lineas: readline() readlines(todas las lineas del archivo mostrarlo como lista)
# with open('files/data1.txt','r',encoding="utf-8") as leer4: 
#   linea1=leer4.readline()
#   linea2=leer4.readline()

# print(linea1, end="")
# print(linea2, end="")
# #convertir en lista
# with open('files/data1.txt','r',encoding="utf-8") as leer5:
#   lista=leer5.readlines()
# print(lista)

# #iterar el archivo
# with open('files/data1.txt','r',encoding="utf-8") as leer6:
#   for i in leer6:
#     print(i,end="")

#     #Escritura w+=borar todos los elementos del archivo
# with open('files/data2.txt',"a+") as escritura:
#   escritura.write("\nEsta es otra linea:abcabcabc")

# with open('files/data2.txt','r') as lectura:
#   datos=lectura.read()
#   print(datos)

# #Escritura de otros tipos de datos
# valores=[1234,5678,91011,3.14]

# with open('files/data3.txt',"w+") as lista:
#   for i in valores:
#     casting=str(i)
#     lista.write(casting)
#     lista.write("\n")
# with open('files/data3.txt','r') as lectural:
#   datosl=lectural.read()
#   print(datosl)


# pensum = [{'0123': {'nombre': 'intro a la ing', 'créditos': 2},'4567': {'nombre': 'inglés', 'créditos': 1}},{}, {}]
# pensum[0]['0123']['nombre']="fundamentos"
# print(pensum)


# #seek: ubicarnos dentro del archivo (#cantidad de caracteres que el va contar,posicion inicial)
# #0 principio del archivo,1(posicion actual),2(al final del archivo)
# with open('files/data4.txt','r') as cursor:
#   cursor.seek(15,0)
#   for linea in cursor:
#     print(linea, end="")
# with open('files/data4.txt','r') as cursor:
#   cursor.seek(0,1)
#   for linea in cursor:
#     print(linea, end="")
# with open('files/data4.txt','r') as cursor:
#   cursor.seek(0,2)
#   for linea in cursor:
#     print(linea, end="")


# #tell(tamaño del archivo) bytes
# with open('files/data4.txt','a+') as tamano: #funcion
#   print(tamano.tell())


# #insertar linea en posicion del archivo
# #1 guardar la linea en una lista
# with open('files/data5.txt','r',encoding="utf-8") as archivo_lista:
#   lista3=archivo_lista.readlines()

# lista3.insert(1,"Esta es una nueva linea insertada\n")

# with open('files/data5.txt','w',encoding="utf-8") as archivo_listaes:
#   contenido="".join(lista3) #serializacion coleccion-archivo deserializacion archivo-coleccion
#   archivo_listaes.write(contenido)

# with open('files/data5.txt','r',encoding="utf-8") as archivo_listale:
#   print(archivo_listale.read())

# #listar los archivos: conocer el tamano de los archivos que tiene un directorio
# import os #version de este python es mayor a la 3.5
# entries =os.scandir("files/")
# for entry in entries:
#   print(entry.name +",esdirectorio:"+ str(entry.is_dir())+",size:"+
#         str(entry.stat().st_size) +"bytes.")


# #serializacion dump pickle .pkl binario wb(escribir binario) rb(leer binario)
# import pickle
# nombres=["Alejandra","Pedro","Santiago"]
# apellido=["Ospina","Perez","Montenegro"]
# diccionario=dict([(clave,valor) for clave,valor in zip(nombres,apellido)])
# with open('files/libreriap.pkl',"wb") as parchivo:
#   pickle.dump(nombres,parchivo)
#   pickle.dump(apellido,parchivo)
#   pickle.dump(diccionario,parchivo)

# #deserealizacion: archivo-coleccion load pickle rb(lectura de binario) wb(escritura de binario)
# import pickle
# with open('files/libreriap.pkl',"rb") as larchivo:
#   nombres1=pickle.load(larchivo)
#   apellidos1=pickle.load(larchivo)
#   diccionario1=pickle.load(larchivo)

# print(nombres1)
# print(apellidos1)
# print(diccionario1)

# #copiar una imagen
# with open('files/discurso.jpg',"rb") as imagen:
#   data=imagen.read()
# with open('files/copia.jpg',"wb") as copia:
#   copia.write(data)

#   #json(javascript)(estandar(intercambio de información entre las aplicaciones) 
# #objeto javascript) archivos 
# #objeto json(diccionarios,claves(cadenas""):
# #valor(estructuras,numeros, valor de verdad(true,false),"",null(None)(nulo),objeto json(recursividad))) codigos
# #valor(True, False)
# import json
# persona={
#     "nombre":"Juan",
#     "apellido":"Gonzalez",
#     "pasatiempos":["futbol","trotar"],
#     "edad":64,
#     "hijos":True,
#     "vehiculo":None
# }
# #Serializacion: proceso de preparacion de una coleccion para un archivo dump
# #archivo(dump), variable(dumps)
# with open('json/nuevo.json','w') as nuevo1:
#   json.dump(persona,nuevo1) #serializacion
# with open('json/nuevo.json','r') as nuevo2:
#   datos=nuevo2.read()
#   print(datos,type(datos))

# #Serialización a variable
# contenido=json.dumps(persona,indent=5) #serializacion
# print(contenido,type(contenido))

# #Deserealizacion convierto un objeto(serializado) a un diccionario (archivo, variable) load(archivos) loads(variable)
# #archivo
# import json
# with open('json/nuevo.json','r') as lectura:
#   datos=json.load(lectura)
# print(datos,type(datos))
# #variable
# dias='''{
#     "lunes":16,
#     "martes":17,
#     "miercoles":18,
#     "jueves":19,
#     "viernes":20
# }'''
# print(type(dias))
# contenido=json.loads(dias)
# print(contenido,type(contenido))

# import json
# import pprint
# generos={
#     "salsa":"Victor Manuel",
#     "bachata":"Romeo",
#     "Regueton":"Jbalvin"
# }

# print(type(generos))
# serializar=json.dumps(generos)
# print(serializar,type(serializar))

# deserializado=json.loads(serializar)
# print(deserializado,type(deserializado))
# pprint.pprint(deserializado)

# import json
# objeto=input()
# print(type(objeto))
# diccionario=json.loads(objeto)
# print(diccionario,type(diccionario))
# #comparaciones

# #desde internet json requests get
# import json #nombre carpeta/archivo as lib
# import requests
# objeto=requests.get("https://jsonplaceholder.typicode.com/todos")
# diccionario=json.loads(objeto.text)
# print(diccionario)

# #Excepciones: manejo de error que interrumpen la ejecución del programa
# #try(intentar) except(excepcion) finally(son instrucciones que si o si se ejecutan)
# num1=int(input("Ingrese el numero"))
# num2=int(input("Ingrese el numero2"))
# try: 
#   division=num1/num2
#   print(division)
# except:
#   print("Ingrese un valor que no sea 0")

# #Valor no apropiado
# numero1=int(input("Ingrese un valor"))
# numero2=int(input("ingrese otro valor"))
# division1=numero1/numero2
# print(division1)

# def division(x,y):
#   try: 
#     division=x/y
#     return division
#   except:
#     print("Ingrese un valor que no sea 0")
#     return ""
# def main():
#   try:
#     numero1=int(input("Ingrese un valor"))
#     numero2=int(input("ingrese otro valor"))
#     print(division(numero1,numero2))
#   except ValueError:
#     print("Ingrese un valor que sirva")
# main()

# #finally
# #usted crea un programa que reciba dos numero y saque las operaciones matematicas(+ - * / // %)
# try: 
#   numero1=int(input("Ingrese un valor"))
#   numero2=int(input("ingrese otro valor"))
#   division=numero1/numero2
#   entera=numero1//numero2
#   residuo=numero1%numero2
#   suma=numero1+numero2
#   resta=numero1-numero2
#   multiplicacion=numero1*numero2
# except:
#   print("El valor no esta bien")
# else:
#   print(division,entera,residuo)
#   print(suma,resta,multiplicacion)
# finally:
#   print("Finalmente esto esta")


# #capturar
# try:
#   num=int(input("Ingrese numero"))
#   resultado=100/num
#   print(resultado)
# except Exception as error:
#   print(error,"\n",type(error))


# #lanzar una excepcion raise ValueError
# def division1(a,b):
#   if b==0:
#     raise ValueError("No se puede dividir por que es por cero")
#   else:
#     resultado=a/b
#     return resultado
# try:
#   x=int(input("Ingrese el valor"))
#   y=int(input("Ingrese el valor"))
#   print(division1(x,y))
# except Exception as creacion:
#   print(creacion,"\n",type(creacion))

# x=int(input("Ingrese el valor"))
# while True:
#   try:
#     y=int(input("Ingrese el valor"))
#     resultado=x/y
#     print(resultado)
#     break
#   except Exception as creacion:
#     print(creacion,"\n",type(creacion))


# lista=[1,2,3,4,5]
# posicion=int(input("Ingrese un numero"))
# try:
#   print(lista[posicion])
# except Exception as valor:
#   print("Intenta acceder a una posicion que no esta en la lista", type(valor))

# def operar(a,b):
#   return a+b

# def main():
#   try:
#     a =int(input())
#     b =int(input())
#     print(operar(a, b))
#   except Exception as suma:
#     print("Los tipos de datos no cuadran para hacer la operacion", type(suma))

# main()

# def main():
#   dict ={"James":"Java","Dennis":"C","Das":"Python"}
#   try:
#     print(dict["Ada"])
#   except Exception as diccionario:
#     print("Intenta acceder a una llave que no esta dentro del diccionario",type(diccionario))
# main()

# #librerias: conjunto de funciones o metodos(porcion de codigo con un rol) asociados a un mismo tema
# #ficheros, tienen un nombre, extension, funciones. librerias por defecto o librerias creadas.
# #no tienen programa principal - para ser ejecutada debe ser importada
# #def tipo_ropa(lista):
#   #"instrucciones"
# import numpy as np
# arreglo=np.array(list(range(1,5)))
# print(arreglo)
# print(type(arreglo))
# print(arreglo.shape) #cantidad elementos,tamaño 
# arreglo[3]=10
# print(arreglo)
# print(arreglo[1])
# arreglo1=np.zeros(10)
# print(arreglo1)

# matriz=np.array([[1,2,3,4],[5,6,7,8]]) #2*4
# print(matriz)
# matriz[0,0]=23
# print(matriz)
# print(matriz.shape)
# matriz1=np.ones((3,3))
# print(matriz1)
# print(matriz[1,0])

# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8]])
# b=np.array([[4,5,6,7],[8,9,10,11]])
# #suma
# print(a+b)
# print(np.add(a,b))
# #raiz cuadrada
# print(np.sqrt(b))
# #linspace crear una matriz con un inicio y un fin cantidad de valores 
# np.linspace(2,3,num=10)

# #matplotlib: graficar datos visualizaciones 2D 3D
# import matplotlib.pyplot as plt
# #grafico lineal plot
# plt.plot([1,2,3,4],[1,4,2,3])


# #grafica en 2d varias funciones(recta,cuadratica,cubica) en 1
# import numpy as np
# import matplotlib.pyplot as plt
# arreglo=np.linspace(0,2,50)
# print(arreglo)
# fig,eje=plt.subplots() #figura,los ejes
# eje.plot(arreglo,arreglo,label="lineal") #grafica lineal
# eje.plot(arreglo,arreglo**2,label="cuadratica")
# eje.plot(arreglo,arreglo**3,label="cubica")
# eje.set_xlabel("Eje X")
# eje.set_ylabel("Eje Y")
# eje.set_title("Grafico")
# eje.legend()

# nombres=["Paula","Ramiro","Sebastian"]
# edades=[30,25,67]

# plt.figure(figsize=(9,3))
# plt.subplot(131)
# plt.bar(nombres,edades)
# plt.subplot(132)
# plt.scatter(nombres,edades)
# plt.subplot(133)
# plt.plot(nombres,edades)

# #pandas manipular grandes volumenes de información entra a trabajar con diccionario DataFrame #BigData
# import pandas as pd
# diccionario={
#     "nombres":["Paula","Andres","Ricardo"],
#     "edades":[30,45,23],
#     "hijos":[2,5,7]
# }
# tabla=pd.DataFrame(diccionario)
# print(tabla)

# #funciones porciones de codigo que realizar un rol especifico 
# #funciones incluidas(len,append,pop,load)
# #funciones definidas por el usario def
# #funciones sin paramatro, con parametro pero sin retorno, con parametro y retorno
# #1. Funciones sin parametro
# def sinparametro():
#   n1=int(input("Ingrese valor"))
#   suma=100+n1
#   print("Tipo 1",suma)
# sinparametro()

# def conparesinre(numero):
#   print("Tipo 2",numero+100)

# num1=int(input("Ingrese valor"))
# conparesinre(num1)

# def conparaconreto(num1,num2):
#   resultado=num1+num2
#   return resultado

# x=int(input("Ingrese numero"))
# y=int(input("Ingrese valor"))
# print("Tipo 3",conparaconreto(x,y))

# #funciones con parametros por defecto
# def suma(x,y=10):
#   return x+y
# c=int(input("Ingrese"))
# resultado=suma(c)
# print(resultado)
# print(suma(4,6)) #por referencia

# #funciones que tienen un numero de parametros como una tupla
# def recorrido(valor,*valor1): #**diccionario
#   print(valor)
#   for val in valor1:
#     print(val)
# recorrido(70)
# recorrido(70,80,90,100)

# #Paso de parametros por referencia
# def extender(l1,l2):
#   l1.extend(l2)

# lista1=[1,2,3,4]
# lista2=[4,5,6,7]
# extender(lista1,lista2)
# print(lista1)


# #locales y globales
# def funcion():
#   global v1
#   print("Local:",v1)
# v1=10
# funcion()
# print(v1)
# #global