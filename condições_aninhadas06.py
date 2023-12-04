from datetime import date
anonasc = int(input('QUAL ANO VOCÊ NASCEU? '))
anoatual = date.today().year
idade =  anoatual - anonasc
print('VOCÊ TEM {} ANOS DE IDADE'.format(idade))
if idade <= 9:
    print('SUA CATEGORIA É MIRIM')
elif idade > 9 and idade <= 14:
    print('SUA CATEGORIA É INFANTIL')
elif idade > 14 and idade <= 19:
    print('SUA CATEGORIA É JUNIOR')
elif idade > 19 and idade <= 20:
    print('SUA CATEGORIA É SÊNIOR')
else:
    print('SUA CATEGORIA É MASTER')