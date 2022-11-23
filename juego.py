import random

c=int(input('Ingrese la cantidad de veces que desea jugar '))

contm=0
contu=0
conte=0

for i in range(c):
    valor=random.randint(0,2)
    print(valor)

    print('//PIEDRA PAPEL O TIJERA//')
    print('0 = PIEDRA ')
    print('1 = PAPEL ')
    print('2 = TIJERA ')
    o=int(input('Ingrese el numero correspondiente '))

    if valor==0 and o==2:
        print('Gano la maquina')
        contm=contm+1
    elif valor==0 and o==1:
        print('Gane yo')
        contu=contu+1
    elif valor==0 and o==0:
        print('Ninguno se hace daño')
        conte=conte+1
    elif valor==1 and o==0:
        print('Gano yo')
        contu=contu+1
    elif valor==1 and o==1:
        print('Ninguno se hace daño')
        conte=conte+1
    elif valor==1 and o==2:
        print('Gano yo')
        contu=contu+1
    elif valor==2 and o==0:
        print('Gano yo')
        contu=contu+1
    elif valor==2 and o==1:
        print('Gano la maquina')
        contm=contm+1
    elif o==2 and valor==2:
        print('Ninguno se hace daño')
        conte=conte+1
print(f'La maquina ganò {contm} veces ')
print(f'Usted ganò {contu} veces ')
print(f'Ninguno se hizo daño {conte} veces')


