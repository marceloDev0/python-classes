num = int(input('DIGITE UM NUMERO ENTRE 0 A 9999: '))
u = num // 1 %10
c = num // 10 % 10
d = num // 100 % 10
m = num // 1000 % 10
print('ANALISANDO O NÚMERO...')
print('unidade: {}'.format(u))
print('dezena: {}'.format(c))
print('centena: {}'.format(d))
print('milhar: {}'.format(m))