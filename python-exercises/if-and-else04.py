salario = float(input('QUAL O VALOR DO SEU SÁLARIO? '))
if salario >= 1250.00:
    novosal = (salario + salario*10/100)
    print('SEU NOVO SÁLARIO É DE: {}'.format(novosal))
else:
    novosal = (salario + salario*15/100)
    print("SEU NOVO SÁLARIO É DE: {}".format(novosal))
print('OBRIGADO POR TRABALHAR AQUI!')