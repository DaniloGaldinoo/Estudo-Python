print ('*'*20)
print ('{:^20}'.format('FATORANDO'))
print ('*'*20)

f = int(input('Insira o numero que deseja o fatorial: '))
totfinal = 1
contador = f

while contador > 1:
    totfinal *= contador
    contador -= 1
print(f'O fatorial de {f} é: {totfinal}')
