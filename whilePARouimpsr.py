from random import randint
vitoria = 0
while True:
    jogador = int(input('diga um número: '))
    computer = randint(0,11)
    total = jogador + computer
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador jogou {computer}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu')
            vitoria += 1
        else:
            print('você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você venceu')
            vitoria += 1
        else:
            print('você perdeu')
            break
    print('vamos jogar novamente...')
print(f'GAMER OVER! você venceu {vitoria} vezes')
    



        

