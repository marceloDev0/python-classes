#faça um programa que leia o comprimento do cateto oposto e do cateto adj e calcule sua hipotenusa
#co = float(input('comprimento do cateto oposto'))
#ca = float(input('comprimento do cateto adjacente'))
#hipo = (co**2 + ca**2)**(1/2)
#print('A hipotenusa vai medir: {:.2f}'.format(hipo))
import math
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente'))
hipo = math.hypot(co, ca)
print('a hipotenusa medir: {:.2f}'.format(hipo))
