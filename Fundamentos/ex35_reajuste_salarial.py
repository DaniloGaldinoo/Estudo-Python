# Exercício 35 - Reajuste Salarial
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o aumento salarial
# aplicando 10% para salários acima de R$ 1250,00
# e 15% para salários iguais ou inferiores.

print('|****************************|')
print('|  *  AUMENTO DE SALARIO  *  |')
print('|****************************|')
sal = float(input(f'Insira o salario atual: R$'))
aum = 0
reaj = 0
if sal > 1250.00:
    aum = sal*0.10
    reaj = sal + aum
else:
    aum = sal*0.15
    reaj = sal + aum

print(f'Seu aumento corresponde à R$:{aum:.2f}\nSendo assim, seu novo salario é de R$:{reaj:.2f}')