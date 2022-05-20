drop table if exists professores;

create table professores (
    id serial primary key,
    nome varchar(100),
    idade integer
);

drop table if exists materias;

create table materias (
    id serial primary key,
    nome varchar(100),
    carga_horaria integer
);

drop table if exists cursos;

create table cursos (
    id serial primary key,
    nome varchar(100),
    quantidade_de_periodos integer
);

drop table if exists blocos;

create table blocos (
    id serial primary key,
    letra varchar(1)
);

drop table if exists andares;

create table andares (
    id serial primary key,
    numero integer,
    bloco_id integer references blocos(id)
);

drop table if exists salas;

create table salas (
    id serial primary key,
    numero integer,
    andar_id integer references andares(id),
    capacidade integer
);

drop table if exists turmas;

create table turmas (
    id serial primary key,
    ano_de_inicio integer,
    semestre_atual integer,
    curso_id integer references cursos(id)
);

drop table if exists alunos;

create table alunos (
    id serial primary key,
    nome varchar(100),
    idade integer,
    turma_id integer references turmas(id)
);

drop table if exists aulas;

create table aulas (
    id serial primary key,
    data_inicio date,
    data_fim date,
    sala_id integer references salas(id),
    professor_id integer references professores(id),
    materia_id integer references materias(id),
    turma_id integer references turmas(id)
);