import random
from time import sleep
print('{:=^40}'.format('JOKENPO'))
usuario = str(input('PEDRA, PAPEL OU TESOURA? '))
lista = 'PEDRA', 'PAPEL', 'TESOURA'
maquina = random.choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('VOCÊ ESCOLHEU {} \nE A MAQUINA ESCOLHEU {}'.format(usuario.upper(), maquina))
if usuario.upper() == 'PEDRA' and maquina == 'PAPEL':
    print('COMPUTADOR VENCEU')
elif usuario.upper() == 'PAPEL' and maquina == 'TESOURA':
    print('COMPUTADOR VENCEU')
elif usuario.upper() == 'TESOURA' and maquina == 'PEDRA':
    print('COMPUTADOR VENCEU')
elif usuario.upper() == 'PEDRA' and maquina == 'TESOURA':
    print('VOCÊ VENCEU')
elif usuario.upper() == 'PAPEL' and maquina == 'PEDRA':
    print('VOCÊ VENCEU')
elif usuario.upper() == 'TESOURA' and maquina == 'PAPEL':
    print('VOCÊ VENCEU')
elif usuario.upper() == maquina:
    print('DEU EMPATE')
