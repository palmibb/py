import json

buys=input()
items=json.loads(buys)
who_buys_9 = input()
who_buys=who_buys_9.split(sep=" ")
cost = []
type_of_item = []
x=0
y=0
for i in who_buys:
    for j in items:
        if i==j:
            cost.append(i)

for k in cost:
    x=items[k]
    type_of_item.append(x)
y=sum(type_of_item)
print(y)
print(cost)