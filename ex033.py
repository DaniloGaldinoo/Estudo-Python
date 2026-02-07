print ('---------------------------')
print('| IDENTIFICADOR DE NUMEROS |')
print ('---------------------------')
n1 = int(input('Insira o 1º numero: '))
n2 = int(input('Insira o 2º numero: '))
n3 = int(input('Insira o 3º numero: '))
nmaior = n1
nmenor = n1

if n1 > nmaior:
    nmaior = n1
else:
    if n2 > nmaior:
        nmaior = n2
    else:
        if n3 > nmaior:
            nmaior = n3
        pass
    pass
pass

if n1 < nmenor:
    nmenor = n1
else:
    if n2 < nmenor:
        nmenor = n2
    else:
        if n3 < nmenor:
            nmenor = n3
        pass
    pass
pass

print(f'O maior numero digitado foi {nmaior}\nO menor numero digitado foi {nmenor}')
