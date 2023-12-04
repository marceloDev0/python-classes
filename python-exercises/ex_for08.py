maior = 0
menor = 0
for c in range(1, 2):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[35mO maior peso lido foi\033[m {}kg'.format(maior))
print('\033[32mO menor peso lido foi\033[m {}kg[m'.format(menor))    