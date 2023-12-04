nota1 = float(input('DIGITE A PRIMEIRA NOTA: '))
nota2 = float(input('DIGITE A SEGUNDA NOTA: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('SINTO MUITO VOCÊ FOI REPROVADO!')
elif media >= 5.0 and media < 7.0:
    print('VOCÊ ESTÁ EM RECUPERACÃO')
else:
    print('PARABÉNS, APROVADO')