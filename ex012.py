print('Desconto de 5%')
vlr = float(input('Insira o valor do produto: '))
desc = vlr*0.05
vlr = vlr-desc
print('O Novo preço do produto com o desconto de 5% é de R$: {:.2f}'.format(vlr))