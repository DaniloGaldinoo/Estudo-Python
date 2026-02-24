# Exercício 16 - Cálculo de aluguel de carro
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o valor total a pagar pelo aluguel de um carro,
# considerando R$60 por dia e R$0,15 por km rodado.

print('Calculadora carro alugado')
kmperc = float(input('Digite quantos km foram percorridos: ' ))
dias = float(input('Insira quantos dias o carro ficou alugado: '))
diaria = 60
km = 0.15

totkm = km * kmperc
totdia = diaria * dias
tot = totkm + totdia

print('O valor é pagar é R$:{:.2f}\nR$:{:.2f} referente aos kms percorridos e R$:{:.2f} referente a quantidade de dias com o veiculo!'.format(tot, totkm, totdia))