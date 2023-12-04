from random import randint
from time import sleep
import emoji
computer = randint(0, 5) #computador randomizar um número
print('-=-' *20)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADVINHAR...')
print( '-=-' *20)
jogador = int(input('EM QUE NÚMERO EU PENSEI? ')) #você tentar advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computer:
    print(emoji.emojize("PARABÉNS! você conseguiu ganhar :sad_but_relieved_face:!!"))
else:
    print('VOCÉ PERDEU HAHA')