#leia o 1 termo de uma pA e a razão depois mostre os 10 primeiros termos
ptermo = int(input('DIGITE O PRIMEIRO TERMO DE UMA PA: '))
razao = int(input('DIGITE A RAZAO DA PA: '))

for c in range(ptermo, 10, razao):
    print(c)