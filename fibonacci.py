ult = 1
pen = 0
termo = 1
count = 0
lista = []
elementos = int(input('Digite a qtd de elementos da sequência Fibonacci quer ver: '))
while count <= elementos - 3:
    if elementos == 2:
        lista.append(0)
        lista.append(1)
        break
    if elementos == 1:
        lista.append(0)
        break
    if elementos == 0:
        print('Fim do programa')
        break
    if count == 0:
        lista.append(0)
        lista.append(1)
    termo = ult + pen
    pen = ult
    ult = termo

    lista.append(termo)

    count += 1

print(*lista)
