import random
import csv

# Lista de pessoas
pessoas = [
    "Alexsandro", "Maah", "Charles", "Guilherme", "Bianca", "Everton", "Franciely",
    "Deziree", "Maria Paula", "Tatiane", "Du", "Gaby", "Domenico", "Gabi Gonzaga",
    "Thais Takeushi", "Thais Miliao", "Bryan", "Shey", "Felipe", "Pedro Barreto",
    "Pronto E.", "Mi", "Paula", "Vitor", "Nicoly", "Maria - Nova", "Paulo - Novo"
]

# Definir os setores
setores = {
    "Assistência": 0,
    "Senha": 0,
    "Álcool": 0,
    "Lago": 0,
    "Cozinha": 0,
    "Setor 1": 0,
    "Setor 2": 0,
    "Setor 3": 0,
    "Setor 4": 0,
    "Casinhas": 0,
    "Criancas": 0,
    "Sala de Cambone": 0
}

# Dicionário para controlar quantas vezes cada pessoa ficou em cada setor
registro = {pessoa: {setor: 0 for setor in setores} for pessoa in pessoas}

# Carregar o registro existente (se houver)
try:
    with open("registro.csv", "r") as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            pessoa = linha["Pessoa"]
            setor = linha["Setor"]
            vezes = int(linha["Vezes"])
            registro[pessoa][setor] = vezes
except FileNotFoundError:
    pass

def atribuir_pessoa_ao_setor(pessoa):
    """Atribui uma pessoa a um setor, evitando repetições frequentes."""
    while True:
        setor = random.choice(list(setores.keys()))
        if setor in ["Lago", "Casinhas", "Álcool", "Senha", "Assistência", "Criancas"]:
            if setores[setor] == 0:
                setores[setor] += 1
                return setor
        elif setor == "Cozinha":
            if setores[setor] < 2:
                setores[setor] += 1
                return setor
        elif setor in ["Setor 1", "Setor 2", "Setor 3", "Setor 4"]:
            if setores[setor] >= 4:
                continue
            # Verificar quantas vezes a pessoa ficou no setor
            vezes_no_setor = registro[pessoa][setor]
            if vezes_no_setor >= 3:  # Evite mais de 3 vezes no mesmo setor
                continue
            setores[setor] += 1
            registro[pessoa][setor] = vezes_no_setor + 1
            return setor
        elif setor == "Sala de Cambone":
            if pessoa in ["Maria - Nova", "Paulo - Novo"]:
                setores[setor] += 1
                return setor

def main():
    """Função principal para atribuir pessoas aos setores e imprimir os resultados."""
    # Embaralhar a lista de pessoas aleatoriamente
    random.shuffle(pessoas)

    # Inicializar um dicionário para armazenar as atribuições
    atribuicoes = {setor: [] for setor in setores}

    # Atribuir pessoas aos setores
    for pessoa in pessoas:
        setor_atribuido = atribuir_pessoa_ao_setor(pessoa)
        atribuicoes[setor_atribuido].append(pessoa)

    # Imprimir as atribuições
    for setor, pessoas_atribuidas in atribuicoes.items():
        print(f"{setor}: {pessoas_atribuidas}")

    # Salvar o registro atualizado no arquivo CSV
    with open("registro.csv", "w", newline="") as arquivo_csv:
        campos = ["Pessoa", "Setor", "Vezes"]
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for pessoa, setores_em_que_ficou in registro.items():
            for setor, vezes in setores_em_que_ficou.items():
                escritor_csv.writerow({"Pessoa": pessoa, "Setor": setor, "Vezes": vezes})

    print("Registro atualizado e salvo.")

if __name__ == "__main__":
    main()
