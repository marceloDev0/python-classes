maior = homens = mulheres = 0
while True:
    print('-' * 20)
    print('\033[0:36:47m cadastro de pesssoas \033[m')
    print('-' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres += 1
    print('-' * 20)
    opcao = str(input('Quer continuar? ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'pessoas com mais de 18 anos {maior}')
print(f'homens: {homens}')
print(f'mulheres com menos de 20: {mulheres}')