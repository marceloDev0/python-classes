from random import randint
computer = randint(0, 10)
print('hmm, acabei de pensar em um número entre o e 10.')
tentativa = 0
acertou = False
while not acertou:
    jogador = int(input('qual o seu palpite? '))
    tentativa += 1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('mais...')
        elif jogador > computer:
            print('menos...')
print('acertou com {} tentativas.'.format(tentativa))



'''from random import randint
cont = 0
computer = randint(0, 10)
while player != computer:   
    player = int(input('Digite um número: '))
    cont += 1
    print('você escolheu {} e o computador {}'.format(player, computer))
    print('tente novamente')
    if player == computer:
        print('parabéns você venceu com {} tentativas'.format(cont))'''
    