continuar = 'S'
valores = []

while continuar == "S":
    num = (int(input('Digite um Valor: ')))
    if num in enumerate(valores):
        print('Valor Duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print ('Valor Adicionado com sucesso...')

    continuar = str(input('Quer continuar? [S/N]')).upper()
print('-='*20)
print(f'Você digitou os valores: {valores.sort()}')