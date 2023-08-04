from random import randint
from time import sleep
comp = randint(0, 5)
print('=' * 40)
print('Tente adivinhar o número que estou pensando...')
print('=' * 40)

user = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO... \n')
sleep(0.5)

print('PARABÉNS VOCÊ GANHOU! \n\nNúmero sorteado {} \nNúmero escolhido {}'.format(comp, user) if comp == user
else 'PERDEU! \n\nNúmero sorteado {} \nNúmero escolhido {}' . format(comp, user))




