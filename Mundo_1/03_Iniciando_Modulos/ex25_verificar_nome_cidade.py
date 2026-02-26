# Exercício 25 - Verificando Nome da Cidade
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que verifica se o nome de uma cidade
# começa com a palavra "Santo".

cidade = str(input('Insira o nome de uma cidade: ')).strip()
if (cidade.lower().split()[0]) == "santo":
    print("O nome da cidade começa com SANTO!")
else:
    print("O nome da cidade NÃO começa com SANTO!")