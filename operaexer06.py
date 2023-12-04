produtoprec = float(input('DIGITE O VALOR DO PRODUTO:' ))
descon = produtoprec * 5/100
print('DESCONTO DE {:3F}'.format(descon))
novopr = produtoprec - descon
print('NOVO PREÇO {:3f}'.format(novopr))