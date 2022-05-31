buyer1=input()
buyer2=input()
urna=input() 
sum1=0
sum2=0
for j in urna:
  if j in buyer1:
    sum1+=1
  if j in buyer2:
    sum2+=1
  if sum1>sum2:
    print("A",end="")
  elif sum2>sum1:
    print("B",end="")
  else:
    print("E",end="")


#mio
# x=input("ingrese los productos: ")
# z=input("ingrese los productos: ")
# y=input("Gerente, ingreso los datos: ")

# q1=0
# q2=0

# for i in y:
#     if i in x:
#         q1+=1
#     if i in z:
#         q2+=1
#     if q1>q2:
#             print("F",end="")
#     elif q1<q2:
#         print("J",end="")
#     else:
#         print("A",end="")