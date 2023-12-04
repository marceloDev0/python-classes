num1 = int(input('primeiro valor: '))
num2 = int(input('segundo valor: '))
num3 = int(input('terceiro valor: '))
#verificando menor valor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num1:
    menor = num3
print('O menor valor digitado foi {}'.format(menor))
#verificando o maior valor
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O maior valor digitado foi {}'.format(maior))