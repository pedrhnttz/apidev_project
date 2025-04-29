from flask_restx import Namespace, Resource, fields
from aluno.alunos_model import get_professores, get_professor_by_id, create_professor, update_professor, delete_professor

professores_ns = Namespace("professores", description = "Operações relacionadas aos professores")

professor_input_model = professores_ns.model("ProfessorInput",{
    "nome": fields.String(required=True, description="Nome do professor"),
    "disciplina": fields.String(required=True, description="Disciplina"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "salario": fields.Float(required=True, description="Salário professor"),

})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "disciplina": fields.String(description="Disciplina ministrada"),
    "idade": fields.Integer(description="Idade do professor"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "salario": fields.Float(description="Salário professor")

})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return get_professores()

    @professores_ns.expect(professor_input_model)
    def post(self):
        """Cria um novo professor"""
        data = professores_ns.payload
        response, status_code = create_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class ProfessoresIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return get_professor_by_id(id_professor)

    @professores_ns.expect(professor_input_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professores_ns.payload
        update_professor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        delete_professor(id_professor)
        return {"message": "Professor excluído com sucesso"}, 200
