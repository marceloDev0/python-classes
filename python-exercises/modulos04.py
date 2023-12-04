#programa que leia o angulo qualquer e mostre na tela seno, cosseno e tangente
import math
angulo = float(input('digitge o angulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {} \ntem seno: {:.2f} \ncosseno {:.2f} \ntangente {:.2f}'.format(angulo, seno, cosseno, tangente))