from datetime import date
ano = int(input('Digite o ano que quer analizar, ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
print('O ano {} é bissexto'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
      else 'O ano {} não é Bissexto.'.format(ano))