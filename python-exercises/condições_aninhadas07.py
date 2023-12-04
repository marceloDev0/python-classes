print('{:=^68}'.format(' LOJAS FERNANDES '))
precoproduto = float(input('O PREÇO DO PRODUTO É: '))
print('''OPÇÕES DE PAGAMENTO: 
[1] Á VISTA DINHEIRO/CHEQUE
[2] Á VISTA NO CARTÃO 
[3] EM 2 VEZES NO CARTÃO 
[4] EM 3 OU MAIS VEZES NO CARTÃO''' )
formadepaga = int(input('QUAL A FORMA DE PAGAMENTO? '))
if formadepaga == 1:
    total = precoproduto - precoproduto *10/100
    print('VOCÊ ESCOLHEU O PAGAMENTO Á VISTA NO DINHEIRO E VAI PAGAR {}R$'.format(total))
elif formadepaga == 2:
    total = precoproduto - precoproduto *5/100
    print('VOCÊ ESCOLHEU O PAGAMENTO Á VISTA NO DINHEIRO E VAI PAGAR {}R$'.format(total))
elif formadepaga == 3:
    print('VOCÊ VAI PAGAR {}R$'.format(precoproduto/2))
elif formadepaga == 4:
    total = precoproduto + precoproduto*20/100
    print('VOCÊ VAI PAGAR {}R$'.format(total))