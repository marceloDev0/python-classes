fatorial = 1
c = int(input('digite um número: '))
print('calculando {}! = '.format(c), end='')
while c > 0: 
    print('{} '.format(c), end='')   
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c = c - 1    
print('{}'.format(fatorial))
