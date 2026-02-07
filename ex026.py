frase = str(input("Escreva uma frase qualquer: ").strip())
print(f'A letra A aparece {frase.lower().count('a')} vezes na frase!')
print(f'A primeira letra A apareceu na posição {frase.lower().find('a')+1}')
print(f'A última letra A apareceu na posição {frase.lower().rfind('a')+1}')