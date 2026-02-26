# Exercício 44 - Classificação de IMC
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o Índice de Massa Corporal (IMC)
# e classifica o resultado conforme tabela padrão.

print ('\033[32m' + '=-' * 11 + '\033[m')
print ('\033[34m' + '* CALCULADORA DE IMC *' + '\033[m')
print ('\033[32m' + '=-' * 11 + '\033[m')

peso = float(input('Insira o peso: '))
alt = float(input('Insira a altura: '))

imc = peso / (alt **2)

if imc < 18.5:
    print(f'Seu IMC é de: {imc:.2f}! Você esta abaixo do peso.')
elif imc >= 18.5 and imc <25:
    print(f'Seu IMC é de: {imc:.2f}! Você esta no peso ideal.')
elif imc >= 25 and imc <30:
    print(f'Seu IMC é de: {imc:.2f}! Você esta em sobrepeso.')
elif imc>= 30 and imc <40:
    print(f'Seu IMC é de: {imc:.2f}! Você esta com Obesidade.')
else:
    print(f'Seu IMC é de: {imc:.2f}! Você esta com Obesidade morbida.')