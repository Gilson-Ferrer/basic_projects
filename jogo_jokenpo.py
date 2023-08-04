from random import randint
from time import sleep

print('-=-'*20)
print('{:=^60}'.format('J O K E N P Ô'))
print('-=-'*20)

jogador = int(input('Escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n'))
comp = randint(1,3)

print('\n\033[36mJO', end=' ')
sleep(1)
print('\033[33mKEN', end=' ')
sleep(1)
print('\033[32mPO!!!')
sleep(1)

if jogador == 1:
    print('\nJogador escolheu PEDRA')
elif jogador == 2:
    print('\nJogador escolheu PAPEL')
elif jogador == 3:
    print('\nJogador escolheu TESOURA')
else:
    print('Comando inexistente!')


if comp == 1:
    print('Computador escolheu PEDRA\n')
elif comp == 2:
    print('Computador escolheu PAPEL\n')
else:
    print('Computador escolheu TESOURA\n')


if jogador == 1 and comp == 3:
    print('\033[32mGANHOU! Pedra quebra tesoura')
elif jogador == 2 and comp == 3:
    print('\033[31mPERDEU! Tesoura corta papel')
elif jogador == 3 and comp == 3:
    print('\033[33mEMPATE! 2 Tesouras')

elif jogador == 1 and comp == 2:
    print('\033[31mPERDEU! Papel embrulha pedra')
elif jogador == 2 and comp == 2:
    print('\033[33mEMPATE! Os dois escolheram papel')
elif jogador == 3 and comp == 2:
    print('\033[32mGANHOU! Tesoura corta papel')

elif jogador == 1 and comp == 1:
    print('\033[33mEMPATE! 2 pedras')
elif jogador == 2 and comp == 1:
    print('\033[32mGANHOU! Papel embrulha pedra')
elif jogador == 3 and comp == 1:
    print('\033[31mPERDEU! Pedra quebra tesoura')
