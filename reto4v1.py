import json

dispo=input()
disponibles=json.loads(dispo)
cliente = input()
cliente=cliente.split(sep=" ")
moneda = []
cuenta = []
a=0
b=0
for i in cliente:
    for j in disponibles:
        if i==j:
            moneda.append(i)

for k in moneda:
    a=disponibles[k]
    cuenta.append(a)
b=sum(cuenta)
print(b)
print(moneda)