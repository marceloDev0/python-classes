print('P.A APLICACION')
print('=-' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro 
c = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while c <= tot:
        print('{} > '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('quanto termos você quer mostrar mais? '))

