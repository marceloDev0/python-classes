#programa que leia um valor em metros e mostre em cemimetros e em milimetros
metro = float(input('DIGITE O VALOR EM METROS '))

cem = metro * 100
mili = metro * 1000

print('{} M EQUIVALE A {} CENTIMETROS E A {} MILIMETROS'.format(metro, cem, mili))