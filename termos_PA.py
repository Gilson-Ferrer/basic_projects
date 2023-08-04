result = 0
count = 0
t = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
qtd_termos = int(input('Quantos termos quer ver? '))
while count < qtd_termos:
    result += r
    count+=1

    print('{}'.format(result), end= ' -> ')
print('ACABOU')
print('\nPA com {} termos'.format(count))
