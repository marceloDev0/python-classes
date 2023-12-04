#programa que leia a velocidade de um carro, se ele ultrapassar 80km mostre uma msg dizendo que ele foi multado
velocidade = float(input('QUAL A VELOCIDADE DO CARRO? '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO DIMINUA A VELOCIDADE!!!')
    multa = (velocidade-80) * 7
    print('VOCÊ VAI PAGAR UMA MULTA DE {:.2f}R$!'.format(multa))
print('tenha um bom dia! diriga com segurança!')

