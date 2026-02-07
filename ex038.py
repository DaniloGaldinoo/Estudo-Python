print ('\033[32m' + '*' * 23 + '\033[m')
print ('\033[34m' + '* COMPARADOR NUMERICO *' + '\033[m')
print ('\033[32m' + '*' * 23 + '\033[m')

n1 = int(input('Insira o primeiro Numero: '))
n2 = int(input('Insira o segundo Numero: '))
maior = n1
menor = n1

if n2 > n1:
    maior = n2

if n2 < n1:
    menor = n2

if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n1 < n2:
    print('O SEGUNDO valor é maior!')
else:
    print('Não existe valor maior, os dois são IGUAIS!.')