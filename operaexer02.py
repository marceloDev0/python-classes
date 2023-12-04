#desenvolva um programa que leia as duas notas de um aluno e mostre sua média

nota01 = float(input('DIGITE A PRIMEIRA NOTA : '))
nota02 = float(input('DIGITE A SEGUNDA NOTA: '))
media = (nota01 + nota02)/2
print('SUA MÉDIA É: {:.2f}'.format(media))
if media >= 7.0:
    print('SUA NOTA FOI BOA! PARABÉNS!')
else:
    print('SUA NOTA FOI RUIM!')