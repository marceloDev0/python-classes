#indice corporal, calculadora
peso = float(input('DIGITE SEU PESO (KG): '))
altura = float(input('DIGITE SUA ALTURA (M): '))
imc = peso / (altura **2)
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('PESO IDEAL, PARABÉNS')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MÓRBIDA, CUIDADO')
print('SEU IMC É: {:.2f}'.format(imc))