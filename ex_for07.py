from datetime import date
maioridade = 0
menoridade = 0
anoatual = date.today().year
for c in range(1, 8):
    data = int(input('DIGITE O ANO DE NASCIMENTO DA {}° PESSSOA: '.format(c)))
    idade =  anoatual - data
    if idade >= 21:
        maioridade = maioridade + 1
    elif idade < 21:
        menoridade = menoridade + 1
print('maioridade: {}'.format(maioridade))
print('menoridade: {}'.format(menoridade))