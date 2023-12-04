import random
al1 = str(input('primeiro nome: '))
al2 = str(input('segundo nome: '))
al3 = str(input('terceiro nome: '))
al4 = str(input('quarto nome: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ORDEM DE APRESENTAÇÃO SERÁ: ')
print(lista)