nome = str(input('DIGITE SEU NOME COMPLETO: ')).strip()
primeiro = nome.split()
print('SEU PRIMEIRO NOME É: {}'.format(primeiro[0]))
print('SEU ÚLTIMO NOME É: {}'.format(primeiro[len(primeiro)-1]))