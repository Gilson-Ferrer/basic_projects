from random import randint
resultado = jogador = comp = cont = 0
while True:
    jogador = int(input('Escolha um número: '))
    escolha = str(input('Quer par ou ímpar [P/I] ')).upper().strip()[0]
    comp = randint(1,2)
    if (jogador + comp) % 2 == 0 and escolha == 'P':
        print('Você GANHOU')
        cont += 1
    if (jogador + comp) % 2 != 0 and escolha == 'I':
        print('Você ganhou')
        cont += 1
    if (jogador + comp) % 2 != 0 and escolha == 'P':
        print('Você PERDEU')
        parada = str(input('Gostaria de parar? s/n ')).upper().strip()[0]
        if parada == 'S':
            break
    if (jogador + comp) % 2 == 0 and escolha == 'I':
        print('Você perdeu')
        parada = str(input('Gostaria de parar? s/n ')).upper().strip()[0]
        if parada == 'S':
            break

print('-==-'*20)
print(f'Você teve {cont} vitória consecutivas')
