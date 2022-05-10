x = int(input('Digite: '))
y = x*2 + 4
z = ((x + y)//5)

print(x)
print(y)
print(z)

if z >=0 and z<=20  :
    print('Uno')
elif z >=21 and z<=30:
    print('Dos')
elif z >=31 and z<=50:
    print('Tres')
elif z >=51:
    print('Cuatro')