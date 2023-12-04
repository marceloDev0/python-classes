while True:
    numero = int(input('quer a tabuada de qual valor? '))
    c = 1
    while c <=10:
        multi = c * numero
        print(f'{c} x {numero} = {multi}')
        c += 1
    if numero < 0:
        break
print('programa encerrado volte sempre!')