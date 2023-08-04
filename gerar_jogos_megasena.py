from time import sleep
from random import randint

jogo = []
lista = []
print('-='*20)
print('               MEGA SENA')
print('-='*20)
resp = int(input('Quantos jogos quer gerar? '))
for i in range (0, resp):
    while True:
        num = randint (1,60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            break

    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
for b in range (0,resp):
    print('Jogo {} = {}'.format(b +1, lista[b]))
    sleep(1)
print()
print('-='*5, 'Boa sorte!', '-='*5)
