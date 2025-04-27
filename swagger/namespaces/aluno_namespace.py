from flask_restx import Namespace, Resource, fields
from aluno.alunos_model import get_alunos, get_aluno_by_id, create_aluno, delete_aluno, update_aluno

alunos_ns = Namespace("alunos", description = "Operações relacionadas aos alunos")