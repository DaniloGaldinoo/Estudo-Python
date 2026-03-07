import csv
import random
from datetime import datetime, timedelta

# Lista de produtos de informática
produtos = [
    ("Notebook", "Computadores", 3500),
    ("Mouse Gamer", "Periféricos", 120),
    ("Teclado Mecânico", "Periféricos", 350),
    ("Monitor 24", "Monitores", 900),
    ("HD 1TB", "Armazenamento", 280),
    ("SSD 480GB", "Armazenamento", 320),
    ("Memória RAM 16GB", "Componentes", 420),
    ("Placa de Vídeo", "Componentes", 2500),
    ("Fonte 600W", "Componentes", 380),
    ("Gabinete Gamer", "Componentes", 450),
    ("Headset Gamer", "Periféricos", 280),
    ("Webcam HD", "Periféricos", 210)
]

clientes = [
    "Carlos Silva", "Ana Souza", "João Pereira", "Mariana Lima",
    "Pedro Santos", "Fernanda Alves", "Lucas Costa", "Juliana Rocha",
    "Rafael Martins", "Camila Barros"
]

cidades = [
    "São Paulo", "Osasco", "Barueri", "Carapicuíba",
    "Santo André", "São Bernardo", "Guarulhos", "Campinas"
]

# Função para gerar data aleatória nos últimos 90 dias
def data_aleatoria():
    hoje = datetime.today()
    dias_atras = random.randint(0, 90)
    data = hoje - timedelta(days=dias_atras)
    return data.strftime("%Y-%m-%d")

# Criar arquivo CSV
with open("vendas_loja_informatica.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)

    # Cabeçalho
    writer.writerow([
        "id_venda",
        "data_venda",
        "produto",
        "categoria",
        "preco_unitario",
        "quantidade",
        "valor_total",
        "cliente",
        "cidade"
    ])

    # Gerar 200 vendas
    for i in range(1, 201):
        produto, categoria, preco = random.choice(produtos)
        quantidade = random.randint(1, 5)
        valor_total = preco * quantidade
        cliente = random.choice(clientes)
        cidade = random.choice(cidades)
        data = data_aleatoria()

        writer.writerow([
            i,
            data,
            produto,
            categoria,
            preco,
            quantidade,
            valor_total,
            cliente,
            cidade
        ])

print("Arquivo vendas_loja_informatica.csv gerado com sucesso!")