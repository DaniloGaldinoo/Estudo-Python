# Exercício 57 - Cadastro e Análise de Pessoas
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Lê nome, idade e sexo de 4 pessoas,
# calcula a média de idade do grupo, identifica
# o homem mais velho e conta quantas mulheres
# têm menos de 20 anos.

print('°{}°'.format('°'*39))
print('°  CADASTRANDO E IDENTIFICANDO PESSOAS  °')
print('°{}°'.format('°'*39))

qtdmulher = 0
ivelho = 0
hvelho = ''
somaidade = 0

for c in range(1, 5):
    nome = input('Insira o nome: ').strip()
    idadeatual = int(input('Insira a idade: '))
    sexo = int(input('[1] MASCULINO | [2] FEMININO\n').strip())

    somaidade += idadeatual

    # Homem mais velho
    if sexo == 1:
        if idadeatual > ivelho:
            ivelho = idadeatual
            hvelho = nome

    # Mulheres com menos de 20
    if sexo == 2 and idadeatual < 20:
        qtdmulher += 1

media = somaidade / 4

print(f'A média da idade do grupo é {media:.1f}')
print(f'O nome do homem mais velho é: {hvelho}')
print(f'A quantidade de mulheres com menos de 20 anos é: {qtdmulher}')