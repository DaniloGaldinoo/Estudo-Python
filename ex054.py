maior = 0
menor = 0

for c in range (1, 8):
    ano = int(input(f'Insira o ano de nascimento da {c}º pessoa: '))
    tot = 2025-ano
    if tot > 18:
        maior += 1
    else:
        menor += 1

print(f'No total temos {maior} maiores de idade e {menor} menores de idade!')