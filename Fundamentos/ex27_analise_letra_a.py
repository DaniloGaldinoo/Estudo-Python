# Exercício 27 - Análise da Letra A
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que analisa uma frase e informa
# quantas vezes a letra "A" aparece, além da posição
# da primeira e da última ocorrência.

frase = str(input("Escreva uma frase qualquer: ").strip())
print(f'A letra A aparece {frase.lower().count('a')} vezes na frase!')
print(f'A primeira letra A apareceu na posição {frase.lower().find('a')+1}')
print(f'A última letra A apareceu na posição {frase.lower().rfind('a')+1}')