diasalugados = int(input('QUANTOS DIAS ALUGADOS?'))
quantikm = float(input('QUANTIDADE DE KM '))
pago = (diasalugados * 60) + (quantikm * 0.15)

print('TOTAL A PAGAR: {}R$'.format(pago))