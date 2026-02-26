# Exercício 45 - Condições de Pagamento
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que aplica desconto ou juros
# ao valor de um produto conforme o método de pagamento escolhido.

print ('\033[32m' + '*~-' * 9 + '\033[m')
print ('\033[34m' + '* CALCULADORA DE DESCONTO *' + '\033[m')
print ('\033[32m' + '*~-' * 9 + '\033[m')

vlr = float(input('Insira o valor do produto: '))
desc = 0
tot = 0
j = 0
print('METODOS DE PAGAMENTO DISPONIVEIS:')
print('[1] - DINHEIRO OU CHEQUE')
print('[2] - CARTÃO A VISTA')
print('[3] - 2x NO CARTÃO')
print('[4] - 3x OU MAIS NO CARTÃO')
pag = int(input('Selecione o metodo de pagamento!'))

if pag == 1:
    desc = vlr * 0.10
    tot = vlr - desc
    print(f'O valor do desconto é de R$:{desc:.2f}\nO valor do produto com o desconto aplicado é de R$:{tot:.2f}')
elif pag == 2:
    desc = vlr * 0.05
    tot = vlr - desc
    print (f'O valor do desconto é de R$:{desc:.2f}\nO valor do produto com o desconto aplicado é de R$:{tot:.2f}')
elif pag == 3:
    print(f'Com essa condição de pagamento o valor do produto é integral. VALOR R$:{vlr:.2f}')
elif pag == 4:
    j = vlr * 0.20
    tot = vlr + j
    print(f'Com essa condição de pagamento, é acrescentado 20% de juros. Segue o novo valor do produto -> R$:{tot:.2f}')
else:
    print('METODO INFORMADO INVALIDO!')
