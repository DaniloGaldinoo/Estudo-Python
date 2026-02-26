# ==========================================================
# Exercício 23 - Análise de Nome Completo
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que analisa um nome completo, exibindo
#            o nome em maiúsculas, minúsculas, total de letras
#            (sem espaços) e quantidade de letras do primeiro nome.
# ==========================================================

nome = input('Digite o seu nome completo: ').strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')

primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome tem {len(primeiro_nome)} letras')