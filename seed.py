import sqlite3
from random import randint, choice
from datetime import datetime, timedelta

blocos = [char for char in "ABCDE"]
NUMERO_DE_PROFESSORES = 200
NUMERO_DE_MATERIAS = 100
NUMERO_DE_CURSOS = 30
NUMERO_DE_BLOCOS = len(blocos)
NUMERO_DE_ANDARES_POR_BLOCO = 5
NUMERO_DE_ANDARES_TOTAL = NUMERO_DE_ANDARES_POR_BLOCO * NUMERO_DE_BLOCOS
NUMERO_DE_SALAS = 500
NUMERO_DE_TURMAS = 400
NUMERO_DE_ALUNOS = 8000
NUMERO_DE_AULAS = 400000

with open("banco.db", "w") as db:
    db.write("")

# connect to sqlite at banco.db
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# run file create_entities.sql inside banco.db
with open("create_entities.sql", "r") as f:
    sql = f.read()
    cursor.executescript(sql)

nomes_possiveis = [
    "Alessandro",
    "Aline",
    "Ana",
    "Bruna",
    "Carlos",
    "Daniel",
    "Eduardo",
    "Fernando",
    "Gustavo",
    "Heitor",
    "Isabela",
    "João",
    "José",
    "Lucas",
    "Mateus",
    "Natália",
    "Pedro",
    "Rafael",
    "Sara",
    "Thiago",
    "Vitor",
    "Wesley",
]
sobre_nomes = [
    "Silva",
    "Souza",
    "Pereira",
    "Oliveira",
    "Martins",
    "Almeida",
    "Costa",
    "Rodrigues",
    "Santos",
    "Lima",
    "Alves",
    "Gonçalves",
    "Carvalho",
    "Ribeiro",
    "Pinto",
    "Cardoso",
    "Barros",
    "Fernandes",
    "Gomes",
    "Mendes",
    "Barbosa",
    "Dias",
    "Carvalho",
    "Santana",
    "Rocha",
    "Pires",
    "Melo",
    "Souza",
    "Nunes",
    "Cunha",
    "Campos",
    "Moreira",
    "Almeida",
]

curso_nomes = ["Engenharia", "Arquitetura", "Ciência"]

curso_sobrenomes = [
    "de Software",
    "de Computação",
    "Mecânica",
    "Matemática",
    "Física",
    "Química",
    "Biológica",
    "Biomédica",
    "Geofísica",
    "Geográfica",
]

materia_nomes = [
    "Banco",
    "Redes",
    "Sistemas",
    "Analise",
    "Programação",
    "Estatística",
    "Física",
    "Química",
    "Biologia",
    "Matemática",
    "Geografia",
    "História",
    "Filosofia",
    "Sociologia",
]

materia_sobrenomes = [
    "de Dados",
    "de Computação",
    "de Mecânica",
    "de Matemática",
    "de Paradoxos Quanticos",
    "de Blockchain",
    "de Web3",
    "de Arquitetura",
    "de Metaverso",
    "de Inteligência Artificial",
    "de Programação",
]


def nome_completo_aleatorio():
    nome = choice(nomes_possiveis)
    qtde_sobrenomes = randint(1, 3)
    nome_completo = nome
    for i in range(qtde_sobrenomes):
        nome_completo += " " + choice(sobre_nomes)
    return nome_completo


def curso_aleatorio():
    return choice(curso_nomes) + " " + choice(curso_sobrenomes)


def materia_aleatoria():
    return choice(materia_nomes) + " " + choice(materia_sobrenomes)


def idade_aleatoria_professor():
    return randint(30, 60)


def idade_aleatoria_aluno():
    return randint(15, 30)


def carga_horaria_aleatoria():
    return choice(range(30, 70, 5))


def capacidade_aleatoria():
    return choice(range(20, 50, 5))


def quantidade_periodos_aleatoria():
    return choice(range(2, 6))


def data_inicio_fim_aleatoria():
    # data_inicio = dia aleatorio entre 1/1/2015 e 31/12/2021 com hora aleatoria entre 09:00 e 21:00
    # data_fim = mesmo dia da data_inicio com a mesma hora adiantada randomicamente de 1 a 3 horas
    data_inicio = datetime(
        randint(2015, 2021), randint(1, 12), randint(1, 28), randint(9, 21), 0
    )
    data_fim = data_inicio + timedelta(hours=randint(1, 3))
    return data_inicio, data_fim


for i in range(NUMERO_DE_PROFESSORES):
    nome_completo = nome_completo_aleatorio()
    idade = idade_aleatoria_professor()
    cursor.execute(
        "INSERT INTO professores (id, nome, idade) VALUES (?, ?, ?)",
        (i, nome_completo, idade),
    )


for i in range(NUMERO_DE_MATERIAS):
    nome_completo = materia_aleatoria()
    carga_horaria = carga_horaria_aleatoria()
    cursor.execute(
        "INSERT INTO materias (id, nome, carga_horaria) VALUES (?, ?, ?)",
        (i, nome_completo, carga_horaria),
    )


for i in range(NUMERO_DE_CURSOS):
    nome_completo = curso_aleatorio()
    quantidade_periodos = quantidade_periodos_aleatoria()
    cursor.execute(
        "INSERT INTO cursos (id, nome, quantidade_de_periodos) VALUES (?, ?, ?)",
        (i, nome_completo, quantidade_periodos),
    )

for i in range(len(blocos)):
    cursor.execute("INSERT INTO blocos (id, letra) VALUES (?, ?)", (i, blocos[i]))

for i in range(NUMERO_DE_SALAS):
    numero = randint(1, int(NUMERO_DE_SALAS / NUMERO_DE_ANDARES_TOTAL))
    capacidade = capacidade_aleatoria()
    andar_id = randint(1, NUMERO_DE_ANDARES_TOTAL)
    cursor.execute(
        "INSERT INTO salas (id, numero, capacidade, andar_id) VALUES (?, ?, ?, ?)",
        (i, numero, capacidade, andar_id),
    )

andar_bloco = [
    [andar_i, bloco_i]
    for andar_i in range(NUMERO_DE_ANDARES_POR_BLOCO)
    for bloco_i in range(NUMERO_DE_BLOCOS)
]

total_index = 0
for andar_i, bloco_i in andar_bloco:
    cursor.execute(
        "INSERT INTO andares (id, numero, bloco_id) VALUES (?, ?, ?)",
        (total_index, andar_i, bloco_i),
    )
    total_index += 1

# for i in range(NUMERO_DE_ANDARES):
#     cursor.execute(
#         "INSERT INTO andares (id, numero, bloco_id) VALUES (?, ?, ?)",
#         (i, i + 1, randint(0, len(blocos) - 1)),
#     )

for i in range(NUMERO_DE_TURMAS):
    ano_de_inicio = randint(2017, 2021)
    curso_id = randint(0, NUMERO_DE_CURSOS - 1)
    cursor.execute(
        "INSERT INTO turmas (id, ano_de_inicio, curso_id) VALUES (?, ?, ?)",
        (i, ano_de_inicio, curso_id),
    )


for i in range(NUMERO_DE_ALUNOS):
    nome_completo = nome_completo_aleatorio()
    idade = idade_aleatoria_aluno()
    turma_id = randint(0, NUMERO_DE_TURMAS - 1)
    cursor.execute(
        "INSERT INTO alunos (id, nome, idade, turma_id) VALUES (?, ?, ?, ?)",
        (i, nome_completo, idade, turma_id),
    )


for i in range(NUMERO_DE_AULAS):
    data_inicio, data_fim = data_inicio_fim_aleatoria()
    sala_id = randint(0, NUMERO_DE_SALAS - 1)
    professor_id = randint(0, NUMERO_DE_PROFESSORES - 1)
    materia_id = randint(0, NUMERO_DE_MATERIAS - 1)
    turma_id = randint(0, NUMERO_DE_TURMAS - 1)
    cursor.execute(
        "INSERT INTO aulas (id, data_inicio, data_fim, sala_id, professor_id, materia_id, turma_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (i, data_inicio, data_fim, sala_id, professor_id, materia_id, turma_id),
    )

conn.commit()
