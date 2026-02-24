# Exercício 78 - Analisando Vogais
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Analisa cada palavra em uma tupla e
# exibe as vogais presentes em cada uma.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

#for i in range (0, len(palavras)):
#    print (palavras[i])
#O DE BAIXO É MAIS ATUAL E POSSIVELMENTE MAIS SIMPLES

for pal in palavras:
    print(f'Na palavra {pal.upper()} temos as seguintes vogais: ', end='')
    for letra in pal:
        if letra.lower() in 'aeiou':
            print (f'{letra} ',end=' ')
    print()
