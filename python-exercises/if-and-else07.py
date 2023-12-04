distancia = float(input('QUAL A DISTANCIA DA SUA VIAGEM? '))
print('você está prestes a começar uma viagem de {:2f}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('e o preço da sua passagem será de R${:.2f}'.format(preco))