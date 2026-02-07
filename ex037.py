print ('\033[32m' + '*' * 22 + '\033[m')
print ('\033[34m' + ' CONVERSOR DE NUMEROS ' + '\033[m')
print ('\033[32m' + '*' * 22 + '\033[m')

n = int(input('Insira o numero que deseja converter: '))
b = 'bin'
o = 'oct'
h = 'hex'

print ('\nTemos disponiveis 3 métodos de conversão! \n')
print ('\033[32m' + '*' * 19 + '\033[m')
print ('\033[34m' + ' [1] - BINARIO ' + '\033[m')
print ('\033[34m' + ' [2] - OCTAL ' + '\033[m')
print ('\033[34m' + ' [3] - HEXADECIMAL ' + '\033[m')
print ('\033[32m' + '*' * 19 + '\033[m')
escolha = int(input('\nEscolha um deles: '))

if escolha == 1:
    print ('\033[34m' + ' BINARIO ' + '\033[m')
    print (f'O numero {n} em binario é: {bin(n)[2:]}')
elif escolha == 2:
    print ('\033[34m' + ' OCTAL ' + '\033[m')
    print (f'O numero {n} em octal é: {oct(n)[2:]}')
elif escolha == 3:
    print ('\033[34m' + ' HEXADECIMAL ' + '\033[m')
    print (f'O numero {n} em hexadeciamal é: {hex(n)[2:]}')
else:
    print('\033[31m' +'OPÇÃO INVALIDA!' + '\033[M')
    