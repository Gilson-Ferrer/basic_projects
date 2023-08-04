
valor = 0
print('-==-'*20)
print('                            BEM VINDO AO BANCO G')
print('-==-'*20)
cont = 'S'
ced50 = ced20 = ced10 = ced01 =0
while cont == 'S':
    valor = float(input('Digite quanto quer sacar: '))
    if valor % 1 == 0:
        ced50 += ((valor // 1) // 50)
        ced20 += ((valor - (ced50 * 50))//20)
        ced10 += ((valor - (ced50 * 50) - (ced20 * 20) ) // 10)
        ced01 += ((valor - (ced50 * 50) - (ced20 * 20) - (ced10 * 10)))
        print('-=-'*20)
        if ced50 > 0:
            print(f'- {ced50:.0f} cédulas de R$ 50,00')
        if ced20 > 0:
            print(f'- {ced20:.0f} cédulas de R$ 20,00')
        if ced10 > 0:
            print(f'- {ced10:.0f} cédulas de R$ 10,00')
        if ced01 > 0:
            print(f'- {ced01:.0f} cédulas de R$ 1,00')

        cont = str(input('Gostaria de fazer outro saque? Digite [S/N]: ')).upper().strip()[0]

        if cont == 'S':
            ced50 = ced20 = ced10 = ced01 = 0

        if cont == 'N':
            print('\nObrigado por utilizar nossos serviços.')
            break

    else:
        print('\033[31mPor favor digite um valor inteiro:\033[m ')
