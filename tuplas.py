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
dia="lunes"
tupla=tuple(dia)
print(tupla)