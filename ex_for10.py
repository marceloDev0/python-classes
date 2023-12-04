frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('não é um palíndromo! ')