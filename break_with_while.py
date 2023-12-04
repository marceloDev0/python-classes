soma = num = 0
while True:
    num = int(input('digite um número: '))
    if num == 999:
        break
    soma += num
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}') # fstrings {soma:.2f}, {jose:^20} centralizar 