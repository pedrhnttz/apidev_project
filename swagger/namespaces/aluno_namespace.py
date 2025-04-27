from flask_restx import Namespace, Resource, fields
from aluno.alunos_model import get_alunos, get_aluno_by_id, create_aluno, delete_aluno, update_aluno

alunos_ns = Namespace("alunos", description = "Operações relacionadas aos alunos")

aluno_input_model = alunos_ns.model("AlunoInput",{
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
})

aluno_output_model = alunos_ns.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "media_final": fields.Float(description="Média das notas do semestre"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista todos os alunos"""
        return get_alunos()

    @alunos_ns.expect(aluno_input_model)
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        response, status_code = create_aluno(data)
        return response, status_code

@alunos_ns.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        """Obtém um aluno pelo ID"""
        return get_aluno_by_id(id_aluno)

    @alunos_ns.expect(aluno_input_model)
    def put(self, id_aluno):
        """Atualiza um aluno pelo ID"""
        data = alunos_ns.payload
        update_aluno(id_aluno, data)
        return data, 200

    def delete(self, id_aluno):
        """Exclui um aluno pelo ID"""
        delete_aluno(id_aluno)
        return {"message": "Aluno excluído com sucesso"}, 200