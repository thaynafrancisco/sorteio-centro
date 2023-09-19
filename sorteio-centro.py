import random
import csv

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

# Criar um dicionário para rastrear quantas vezes cada pessoa ficou em um setor
vezes_que_ficou = {nome: 0 for nome in nomes}

# Calcula o número total de vagas disponíveis
vagas_disponiveis = sum(divisao.values())

# Verifica se o número total de vagas é suficiente para acomodar todas as pessoas
if vagas_disponiveis < pessoas:
    print("Não há vagas suficientes para acomodar todas as pessoas.")
else:
    # Distribui aleatoriamente as pessoas nas categorias e atualiza as vezes que cada pessoa ficou em um setor
    random.shuffle(nomes)
    gerenciamento_de_setores = {categoria: [] for categoria in divisao.keys()}
    for categoria, vagas in divisao.items():
        for _ in range(vagas):
            if nomes:
                pessoa = nomes.pop()
                gerenciamento_de_setores[categoria].append(pessoa)
                vezes_que_ficou[pessoa] += 1

    # Distribui as pessoas restantes na "Sala de Cambone" e atualiza as vezes que cada pessoa ficou em um setor
    while nomes:
        pessoa = nomes.pop()
        gerenciamento_de_setores["Sala de Cambone"].append(pessoa)
        vezes_que_ficou[pessoa] += 1

    # Imprime a distribuição no terminal
    for categoria, pessoas_na_categoria in gerenciamento_de_setores.items():
        print(f"Setor: {categoria}")
        print("Nomes:", ", ".join(pessoas_na_categoria))
        print()  # Adicione uma linha em branco entre os setores

    # Salva os resultados em um arquivo CSV com ponto e vírgula como delimitador
    with open("gerenciamento_de_setores.csv", mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Nome", "Setor", "Vezes que ficou"])
        for categoria, pessoas_na_categoria in gerenciamento_de_setores.items():
            for pessoa in pessoas_na_categoria:
                writer.writerow([pessoa, categoria, vezes_que_ficou[pessoa]])

    print("Resultados salvos no arquivo 'gerenciamento_de_setores.csv'.")
