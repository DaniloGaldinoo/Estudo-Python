n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20 (ZERO para sair): '))
    if num <0 or num >20:
        print ('-'*31)
        print('Tente Novamente.')
        continue
    elif num ==0:
        print ('Você digitou o Numero Zero!\nSaindo . . .')
        break
    else:
        print (f'Você digitou o número {n[num]}')