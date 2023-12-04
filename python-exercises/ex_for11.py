velho = 0
cont = 0
mdidade = 0
nomevelho = ''
for c in range(1, 5):
    print('----- {}° -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).strip()
    mdidade += idade
    if c == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1 

print('Média de idade do grupo: {}'.format(mdidade/4))
print('o homen mais velho é {} e tem {} anos'.format(nomevelho, velho ))
print('Mulheres com menos de 20 anos: {}'.format(cont))