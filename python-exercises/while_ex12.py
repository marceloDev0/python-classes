soma = maior = menor = cont = 0
pessoa = ''
while True:
    nomep = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: '))
    cont += 1
    soma += preco
    if preco > 1000:
        maior = maior + 1
    if cont == 1 or preco < menor:
        menor = preco
        pessoa = nomep
    opcao = ' '
    while opcao not in 'SN':
         opcao = str(input(' Quer continaur? ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total gasto na compra {soma}')
print(f'Produtos que custam mais de 1000: {maior}')
print(f'nome do produto mais barato {pessoa} e preço {menor}')
