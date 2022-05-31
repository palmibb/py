# Durante un encuentro de la Copa Minitas se enfrentan dos equipos, el equipo A y el equipo B, cada uno de ellos registra a sus jugadores para el partido, con la inicial del nombre. Por ejemplo:
# Equipo A: Felipe, Carlos, Andres, Santiago, Pedro. El equipo registra FCASP
# Equipo B: Edgar, Ivan, Jerónimo, Bruno, Ricardo. El equipo registra EIJBR
# Se realizo el encuentro y los goles anotados quedaron en la siguiente tabla:

# EJEMPLOS:
# Entrada                                           Salida
# F F I E E P P S S F                               F I E P S F
#                                                   2 1 2 2 2 1

# B B B B B B A A S P J I I R R F F F F F B         B A S P J I R F B
#                                                   6 2 1 1 1 2 2 5 1

# x=input("Ingrese los datos de los jugadores que hicieron goles: ")
# y=0

from itertools import groupby


x=input("ingresa x: ")
y=x.split()
z=[]
t=len(y)
z.append(y[0])

for i in range(t):
    if(i-1 != -1):
        if(y[i-1] != y[i]):
            z.append(y[i])
print(" ".join(z))

c=[sum(1 for h in q)for h, q in groupby(y)]
print(" ".join(map(str,c)))