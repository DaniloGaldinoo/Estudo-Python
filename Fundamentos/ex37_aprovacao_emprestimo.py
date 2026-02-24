# Exercício 37 - Aprovação de Empréstimo
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o valor da prestação
# de um financiamento imobiliário e verifica se ela
# ultrapassa 30% do salário do comprador.

print ('\033[31m' + '-'*17 + '\033[m')
print ('\033[31m' + '|' + '\033[m' + '\033[7;30;41m' +'   B A N C O   ' + '\033[m' + '\033[31m' + '|' + '\033[m')
print ('\033[31m' + '-'*17 + '\033[m')

vlr = float(input('Insira o valor da propriedade a ser adquirida: R$: '))
sal = float(input('Informe o valor do salario do comprador: R$: '))
percentsal = sal * 0.30
ano = float(input('Em quanto tempo ele pretende pagar? : '))
mes = ano * 12

prest = vlr/mes

print (f'\nValor da prestação mensal: R$ {prest:.2f}')
print (f'Limite permitido (30% do salario): R$ {percentsal:.2f}\n')
if prest > percentsal:
    print ('\033[31m' + 'O VALOR DA PRESTAÇÃO ULTRAPASSA OS 30% REFERENTE AO SALARIO!\nSENDO ASSIM: EMPRESTIMO NEGADO!!!' + '\033[m')
else:
    print('\033[32m' + '*' * 28 + '\033[m')
    print ('\033[32m' + '|' + '\033[m' + '\033[7;32;40m' +'   EMPRESTIMO CONCEDIDO   ' + '\033[m' + '\033[32m' + '|' + '\033[m')
    print('\033[32m' + '*' * 28 + '\033[m')
