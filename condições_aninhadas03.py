numero1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
numero2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
if numero1 > numero2:
    print('{} É MAIOR QUE O SEGUNDO {}'.format(numero1, numero2))
elif numero2 > numero1:
    print('{} É MAIOR QUE O PRIMEIRO {}'.format(numero2, numero1))
else:
    print('OS VALORES SÃO IGUAIS')