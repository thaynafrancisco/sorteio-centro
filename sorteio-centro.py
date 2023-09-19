import random

# Lista de pessoas
nomes = [
    "Alexsandro", "Maah", "Charles", "Guilherme", "Bianca", "Everton", "Franciely",
    "Deziree", "Maria Paula", "Tatiane", "Du", "Gaby", "Domenico", "Gabi Gonzaga",
    "Thais Takeushi", "Thais Miliao", "Bryan", "Shey", "Felipe", "Pedro Barreto",
    "Pronto E.", "Mi", "Paula", "Vitor", "Nicoly", "Maria", "Paulo"
]

pessoas = 25

divisao = {
    "Assistência": 1,
    "Senha": 1,
    "Álcool": 1,
    "Lago": 1,
    "Cozinha": 2,
    "Setor 1": 4,
    "Setor 2": 4,
    "Setor 3": 4,
    "Setor 4": 4,
    "Casinhas": 1,
    "Criancas": 1,
    "Sala de Cambone": 1
}

# Calcula o número total de vagas disponíveis
vagas_disponiveis = sum(divisao.values())

# Verifica se o número total de vagas é suficiente para acomodar todas as pessoas
if vagas_disponiveis < pessoas:
    print("Não há vagas suficientes para acomodar todas as pessoas.")
else:
    # Distribui aleatoriamente as pessoas nas categorias
    random.shuffle(nomes)
    distribuicao = {categoria: [] for categoria in divisao.keys()}
    for categoria, vagas in divisao.items():
        for _ in range(vagas):
            if nomes:
                pessoa = nomes.pop()
                distribuicao[categoria].append(pessoa)

    # Distribui as pessoas restantes na "Sala de Cambone"
    while nomes:
        pessoa = nomes.pop()
        distribuicao["Sala de Cambone"].append(pessoa)

    # Imprime a distribuição
    for categoria, pessoas_na_categoria in distribuicao.items():
        print(f"{categoria}: {', '.join(pessoas_na_categoria)}")
