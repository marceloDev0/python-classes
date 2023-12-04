lado1 = float(input('PRIMEIRO LADO: '))
lado2 = float(input('SEGUNDO LADO: '))
lado3 = float(input('TERCEIRO LADO: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('É POSSÍVEL FORMAR UM TRIAGULO ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('OS SEGMENTOS NÃO FORMAM UM TRIÂNGULO!!!')
