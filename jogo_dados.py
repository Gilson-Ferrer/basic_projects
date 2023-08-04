from random import randint
from time import sleep
jogadores = {}
lista = []

cont = 0
for i in range(0,4):
    jogadores[cont] = randint(1,6)
    lista.append(jogadores.copy())
    jogadores.clear()
    cont += 1
cont = 0
for i, v in enumerate(lista):
    print(f'O jogador {i +1} tirou {lista[i][cont]}')
    cont +=1
    sleep(0.5)
print('-='*30)
print('                         GANHADOR')
print('-='*30)

#for r, p in enumerate(lista):
print(f'1º colocado com {max(lista[0][0],lista[1][1],lista[2][2],lista[3][3])}')
#print(f'2º colocado com {}')
# print(f'1º colocado com {max(lista[0]["jogador"],lista[1]["jogador"],lista[2]["jogador"],lista[3]["jogador"])}')
