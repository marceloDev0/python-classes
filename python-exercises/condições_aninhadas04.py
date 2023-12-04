from datetime import date
sexo = str(input('QUAL O SEU SEXO MASCULINO OU FEMENINO '))
if sexo == 'feminino':
    print('você não precisa se alistar')
else:
    datadenasc = int(input('EM QUE ANO VOCÊ NASCEU? '))
    anoatual = date.today().year
    idade = anoatual - datadenasc
    if idade < 18:
        falta = 18 - idade
        print('VOCÊ AINDA NÃO ESTÁ APTO A SE ALISTAR FALTAM {} ANOs'.format(falta))
    elif idade > 18:
        passou = idade - 18
        print('VOCÊ PASSOU DO PERIODO DE ALISTAMENTO JÁ FAZ {} ANOs'.format(passou))
    else:
        print('ESTÁ NA HORA DE VOCÊ SE ALISTAR!!!')