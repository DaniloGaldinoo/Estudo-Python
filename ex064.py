print ('*'*18)
print ('{:^20}'.format('  CONTA E SOMA!  '))
print ('*'*18)

cont = 1
soma = 0
num = 0

while num != 999:
    if cont == 1:
        num = int(input('Insira o primeiro numero, ou ' + '\033[31m' + '[999] para SAIR:' + '\033[m' + ' -> '))
        cont += 1
        soma = soma + num
    else:
        num = int(input(f'Insira o {cont} numero: '))
        cont += 1
        soma = soma + num
print(f'Você inseriu {cont-2} numeros e a soma deles foi: {soma-999}')
print('S A I N D O . . .')
