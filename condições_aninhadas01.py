nome = str(input('QUal é o seu nome '))
if nome == 'marcelo':
    print('Que nome lindo')
elif nome == 'pedro' or nome == 'maria':
    print('Seu nome é bem popular')
else:
    print('seu nome é bem normal')
print('tenha um bom dia, {}!'.format(nome))