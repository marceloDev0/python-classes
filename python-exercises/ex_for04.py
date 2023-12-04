#ler 6 numeros e mostra a soma dos pares
s = 0
for c in range(1, 7):
    numero = int(input('DIGITE UM NUMERO QUALQUER: '))
    if numero%2==0:
        s = s + numero
print('A SOMA FOI: {}'.format(s))