soma = 0
num = 1
for c in range (1, 7):

    n = int(input(f'Insira o {num}º numero: '))
    num += 1
    if n % 2 == 0:
        soma += n
print(f'A soma total é: {soma}')