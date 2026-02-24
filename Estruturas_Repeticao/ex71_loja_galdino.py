# Exercício 71 - Loja Galdino
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Registra produtos e preços, calcula o total
# da compra, quantos produtos custam mais de R$1000
# e identifica o produto mais barato.

print ('*'*22)
print ('{:^22}'.format('*    LOJA GALDINO    *'))
print ('*'*22)
total = np = 0
maisbarato = 0
nomebarato = ''
s = 'S'

while s == 'S':
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco

    if preco > 1000:
        np += 1

    if maisbarato == 0 or preco < maisbarato:
        maisbarato = preco
        nomebarato = produto

    s = str(input('Quer continuar? [S/N] : ')).strip().upper()[0]

print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi de R$: {total:.2f}')
print(f'Temos {np} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R$:{maisbarato:.f}')