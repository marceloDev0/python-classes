sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('dados invalidos digite novamente: [M/F]')).strip().upper()[0]
print('sexo {} registrado.'.format(sexo))
   
        