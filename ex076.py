listagem = ('Lápis', 1.75,'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print ('-'*55)
print ('LISTAGEM DE PREÇOS'.center(55))
print ('-'*55)

for i in range (0, len(listagem),2):
    produto = listagem[i]
    valor = listagem[i + 1]
    ## A LINHA DE BAIXO É O SEGUINTE: PRODUTO É O NOME DO PRODUTO/ O PONTO DEPOIS DO : SIGNIFICA PREENCHER COM '.' O < É PARA ALINHAMENTO NA ESQUERDA E O 40 É A QTD DE ESPAÇOS QUE OCUPA TAL PARTE.
    ## R$ FOI PRA FORA DA FORMATAÇÃO PARA FICAR ALINHADO DEPOIS DO QUE FOI DEFINIDO NA FORMATAÇÃO(40).
    ## VALOR É O PREÇO DO PRODUTO, > ALINHA A DIREITA, E O TOTAL DEFINIDO FOI 7 ESPAÇOSM COM UMA FORMATAÇÃO FLOAT DE 2 NUMEROS APOS A VIRGULA.
    print (f'| {produto:.<40}R$: {valor:>7.2f} |')
print('-' * 55)
