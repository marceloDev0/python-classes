fibonacci = int(input('Quantos termos quer mostrar? '))
fib = 0
fib2 = 1
c =3
print('{} -> {}'.format(fib, fib2), end='')
while c <= fibonacci:
    fib3 = fib + fib2
    print(' -> {} '.format(fib3), end='')
    fib = fib2
    fib2 = fib3
    c += 1