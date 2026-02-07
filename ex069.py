print ('*'*29)
print ('{:^22}'.format('*    CADASTRE UMA PESSOA    *'))
print ('*'*29)
s = 'S'
maiores = 0
men = 0
mulhermenor = 0

while s == 'S':
    idade = int(input('Idade: '))

    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('Valor invalido. Digite apenas M ou F.')
    print('-'*29)
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        men += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1

    s = str(input('Quer continuar? [S/N] :')).upper().strip()[0]
    print('-' * 29)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {men} homens cadastrados.')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos')