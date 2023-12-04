#programa que calcule a soma de todos os numeros impares multiplos de 3 no intervalo de 1 ate 500
cont = 0
s = 0
for c in range(1, 501, 2):
    if c%3 ==0:
        cont = cont + 1
        s = s + c
print('A SOMA DESSES {} NÚMEROS É IGUAL A: {}'.format(cont, s))