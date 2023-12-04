opcao = 'S'
soma = maior = menor = cont = 0
while opcao != 'N': 
    num = int(input('digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('quer continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print('voce digitou {} números e a média foi {}'.format(cont, media ))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))