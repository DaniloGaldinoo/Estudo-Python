# Exercício 32 - Cálculo de Custo de Viagem
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o valor da passagem
# com base na distância da viagem.

print ('-------------------------')
print ('| * CALCULO DA VIAGEM * |')
print ('-------------------------')
km = float(input('Insira quantos kilometros tem a viagem: '))
vlr = 0

if km <= 200:
    vlr = km * 0.50
else:
    vlr = km * 0.45

print(f'O valor da passagem é R$:{vlr:.2f}')