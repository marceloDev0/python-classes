valorcasa =float(input('Qual o valor da casa? '))
salariocomprador = float(input('Qual é o seu salário? '))
anosdepagamento = int(input('Em quantos anos desejar pagar? '))
prestação = valorcasa/(anosdepagamento * 12)
salario = salariocomprador * 30 / 100
if prestação > salario:
    print('EMPRÉSTIMO NEGADO!!!')
elif prestação <= salario:
    print('EMPRÉSTIMO APROVADO!!!')
    print('VOCÊ VAI PAGAR A CASA EM {:.0f} ANOS COM PRESTAÇÕES DE {:.2f}R$ MENSAIS'.format(anosdepagamento, prestação))
    