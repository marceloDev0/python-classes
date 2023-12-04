num = int(input('Digite um numero inteiro: '))
print(''' ESCOLHA UMA DAS BASES PARA CONVERSÃO
[ 1 ] CONVERTER PARA BINARIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVETER PARA HEXADECIMAL''')
opcao = int(input('SUA OPÇÃO: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))