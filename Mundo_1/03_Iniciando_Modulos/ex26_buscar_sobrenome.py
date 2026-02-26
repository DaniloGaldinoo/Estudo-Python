# Exercício 26 - Verificando Sobrenome
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que verifica se o nome digitado
# contém o sobrenome "Silva".

nome = str(input('Insira seu nome completo: ')).strip()
print('silva' in nome.lower())