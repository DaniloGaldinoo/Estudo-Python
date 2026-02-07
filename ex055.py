for c in range (1, 6):
    peso = float(input(f'Insira o peso da {c}ª pessoa: '))

    if c == 1:
        maior = menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print (f'O maior peso foi {maior} KG e o menor foi {menor} KG!')
