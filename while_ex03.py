from time import sleep
c = 0
num = int(input('DIGITE O PRIMEIRO NÚMERO: '))
num2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
while c != 5:
    print('[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa')
    c = int(input('QUAL OPÇÃO QUER ESCOLHER? '))
    if c == 1:
        soma = num + num2
        print('A SOMA DOS VALORES É {}'.format(soma))
    elif c == 2:
        multi = num * num2
        print('A MULTIPLIÇÃO DOS VALORES É {}'.format(multi))
    elif c == 3:
        if num > num2:
            maior = num
            
        else:
            maior = num2
        print('O MAIOR É {}'.format(maior))
    elif c == 4:
        print('informe os valores novamente')
        num = int(input('DIGITE O PRIMEIRO NÚMERO: '))
        num2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
    elif c == 5:
        print('finalizando...')
        
    else:
        print('opção inválida tente novamente...')
    sleep(2)