nome = str(input('digite seu nome: ')).lower().strip()
print('A LETRA "a" aparece {} vezes'.format(nome.count('a')))
print('A PRIMEIRA LETRA A APARECE NA POSIÇÃO {}'.format(nome.find('a')+1))
print('A ÚLTIMA LETRA A APARECE NA POSIÇÃO {}'.format(nome.rfind('a')+1))
