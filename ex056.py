print('°{}°'.format('°'*39))
print('°  CADASTRANDO E IDENTIFICANDO PESSOAS  °')
print('°{}°'.format('°'*39))

qtdmulher = 0
ivelho = 0
somaidade = 0

for c in range (1, 5):
    nome = str(input('Insira o nome: ')).strip()
    idadeatual = int(input('Insira a idade: '))
    print ('Insira o sexo:')
    sexo = int(input('[1] MASCULINO | [2] FEMININO\n')).strip()

    if c == 1:
        hvelho = nome
        ivelho = idadeatual
    else:
        if idadeatual > ivelho and sexo == 1:
            hvelho = nome
            ivelho = idadeatual
        if sexo == 2 and idadeatual < 20:
            qtdmulher += 1

    somaidade = somaidade + idadeatual


print (f'A media da idade do grupo é {somaidade / 4}')
print (f'O nome do homem mais velho é : {hvelho}')
print (f'A quantidade de mulheres com menos de 20 anos é: {qtdmulher}')
