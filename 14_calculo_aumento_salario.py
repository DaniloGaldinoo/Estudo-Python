# Exercício 14 - Cálculo de aumento salarial
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o novo salário de um funcionário com aumento de 15%.

print('Aumento de 15% no salário')
sal = float(input('Insira o salario atual do funcionario que receberá o aumento: '))
aumento = sal*0.15
sal = sal+aumento
print('O salario reajustado com o aumento de 15% ficou em: R$:{:.2f}'.format(sal))