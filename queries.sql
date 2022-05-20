-- quais sao os nomes de todos os professores?
select
       nome
from
       professores;

-- listar todas as materias em ordem de carga horaria
select
       nome,
       carga_horaria
from
       materias
order by
       carga_horaria;

-- listar todos os cursos em ordem alfabetica
select
       nome,
       quantidade_de_periodos
from
       cursos
order by
       nome;

-- quais sao todos os blocos?
select
       letra
from
       blocos;

-- quais sao todos os andares e em qual bloco estao?
select
       numero,
       letra
from
       andares
       join blocos on andares.bloco_id = blocos.id;

-- quais sao as salas, em qual andar e em qual bloco estao?
select
       salas.numero as numero_da_sala,
       andares.numero as numero_do_andar,
       blocos.letra as letra_do_bloco
from
       salas
       join andares on salas.andar_id = andares.id
       join blocos on andares.bloco_id = blocos.id;

-- quais sao as turmas, em qual ano, semestre e em qual curso estao?
select
       turmas.ano_de_inicio as ano_de_inicio,
       cursos.nome as nome_do_curso
from
       turmas
       join cursos on turmas.curso_id = cursos.id;

-- quais sao os alunos, em qual turma e em qual curso estao?
select
       alunos.nome as nome_do_aluno,
       turmas.ano_de_inicio as ano_de_inicio,
       cursos.nome as nome_do_curso
from
       alunos
       join turmas on alunos.turma_id = turmas.id
       join cursos on turmas.curso_id = cursos.id;

-- quais sao as aulas, em qual data, em qual sala, com qual professor, com qual materia e em qual turma estao?
select
       aulas.data_inicio as data_inicio_aula,
       aulas.data_fim as data_fim_aula,
       salas.numero as numero_da_sala,
       andares.numero as numero_do_andar,
       blocos.letra as letra_do_bloco,
       professores.nome as nome_do_professor,
       materias.nome as nome_da_materia,
       cursos.nome as nome_do_curso,
       turmas.ano_de_inicio as ano_de_inicio_da_turma
from
       aulas
       join salas on aulas.sala_id = salas.id
       join andares on salas.andar_id = andares.id
       join blocos on andares.bloco_id = blocos.id
       join professores on aulas.professor_id = professores.id
       join materias on aulas.materia_id = materias.id
       join turmas on aulas.turma_id = turmas.id
       join cursos on turmas.curso_id = cursos.id;

-- quais sao todas as aulas que o aluno de id 0 precisa frequentar?
select
       alunos.nome as nome_aluno,
       aulas.data_inicio as data_inicio_aula,
       aulas.data_fim as data_fim_aula,
       salas.numero as numero_da_sala,
       andares.numero as numero_do_andar,
       blocos.letra as letra_do_bloco,
       professores.nome as nome_do_professor,
       materias.nome as nome_da_materia,
       cursos.nome as nome_do_curso
from
       alunos
       join turmas on alunos.turma_id = turmas.id
       join cursos on turmas.curso_id = cursos.id
       join aulas on turmas.id = aulas.turma_id
       join salas on aulas.sala_id = salas.id
       join andares on salas.andar_id = andares.id
       join blocos on andares.bloco_id = blocos.id
       join professores on aulas.professor_id = professores.id
       join materias on aulas.materia_id = materias.id
where
       alunos.id = 0
order by
       data_inicio_aula;