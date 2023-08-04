n = int(input('Digite a tabuada que quer: '))

for i in range(1, 11):
      print('{} x {} = {}'.format(n, i, n*i))


# loop inverso

n = int(input('Digite a tabuada que quer: '))

for i in range(10, 0, -1):
    print(n,'x', i,'=', n*i)
