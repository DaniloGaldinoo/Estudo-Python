resp = 'S'

while resp == 'S':
    sexo = str(input('Insira o sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        print('O sexo informado foi MASCULINO!')
    elif sexo == 'F':
        print ('O sexo informado foi FEMININO!')
    else:
        print ('ENTRADA INVALIDA, Tente novamente')
    resp = str(input('Deseja continuar? [S/N]: ')).upper()