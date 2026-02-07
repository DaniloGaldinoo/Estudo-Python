print('|*****************************|')
print('|  *  FORMAÇÃO TRIANGULAR  *  |')
print('|*****************************|')
a = float(input('Insira o valor da primeira reta: '))
b = float(input('Insira o valor da segunda reta: '))
c = float(input('Insira o valor da terceira reta: '))

if a < b+c and b < a+c and c < a+b:
    print('Esses valores FORMAM UM TRIANGULO!')
else:
    print('NÃO FORMAM UM TRIANGULO')