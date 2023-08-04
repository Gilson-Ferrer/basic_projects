from random import randint

tentativas = 0

while True:
    chute = int(input('Digite um número de 0 a 3: '))
    comp = randint(0, 3)
    if chute == comp:
        print('\033[33m             GANHOU\033[m!!')
        print('O numero sorteado foi {}, e você escolheu {}'.format(comp, chute))
        tentativas += 1
        break
    else:
        tentativas += 1
        print('O numero sorteado foi {}, e você escolheu {}'.format(comp, chute))
print('Conseguiu com {} tentativas'.format(tentativas))
