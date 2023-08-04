alt = float(input('Digite sua altuma em cm: '))
peso = float(input('Digite seu pesoem kg: '))
IMC = peso / ((alt/100)**2)

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC  <= 25:
# elif 18.5 <= IMC < 25
    print('Peso Ideal')
elif IMC <= 30:
    # elif 25 <= IMC < 30
    print('Sobrepeso')
elif IMC <= 40:
    # elif 30 <= IMC < 40
    print('Obeso')
else:
    print('Obesidade mórbida')
