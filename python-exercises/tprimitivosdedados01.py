#faça um programa que leia algo pelo teclado e mostre na tela seu tipo e todas as informações possiveis dele
a = input('Digite algo')
print(' tipo primitivo desse valor é', type(a))
print('tem espaços? ', a.isspace())
print('é um numero? ', a.isnumeric())
print('é letra? ', a.isalpha())
print('é maiuscula? ', a.isupper())
print('é minuscula? ', a.islower())
print('é alpla numérico? ', a.isalnum())