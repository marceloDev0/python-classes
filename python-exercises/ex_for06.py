primeiro = int(input('primeiro termo: '))
razao = int(input('razâo: '))
decimo = primeiro +(10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end=' -> ')
print('FIM')