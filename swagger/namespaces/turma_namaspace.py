from flask_restx import Namespace, Resource, fields
from turma.turmas_model import get_turmas, get_turma_by_id, create_turma, update_turma, delete_turma

turmas_ns = Namespace("turmas", description = "Operações relacionadas as turmas")

turmas_input_model = turmas_ns.model("turmasInput",{
    "nome": fields.String(required=True, description="Nome do turmas"),
    "materia": fields.String(required=True, description="Materia"),
    "descricao": fields.String(required=True, description="Descricao"),
    "ativo": fields.Integer(required=True, description="Ativo/Não ativo"),
    "professor_id": fields.Integer(required=True, description="Id do professor da classe")

})

turmas_output_model = turmas_ns.model("turmasOutput", {
    "id": fields.Integer(description="ID da turma"),
    "nome": fields.String(description="Nome do turmas"),
    "materia": fields.String(description="materia do turmas"),
    "descricao": fields.String(required=True, description="Descricao"),
    "ativo": fields.Integer(required=True, description="Ativo/Não ativo"),
    "professor_id": fields.Integer(required=True, description="Id do professor da classe")


})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self):
        """Lista todas as turmas"""
        return get_turmas()

    @turmas_ns.expect(turmas_input_model)
    def post(self):
        """Cria uma nova turma"""
        data = turmas_ns.payload
        response, status_code = create_turma(data)
        return response, status_code

@turmas_ns.route("/<int:id_turma>")
class TurmasIdResource(Resource):
    @turmas_ns.marshal_with(turmas_output_model)
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        return get_turma_by_id(id_turma)

    @turmas_ns.expect(turmas_input_model)
    def put(self, id_turma):
        """Atualiza uma turma pelo ID"""
        data = turmas_ns.payload
        update_turma(id_turma, data)
        return data, 200

    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        delete_turma(id_turma)
        return {"message": "Turma excluída com sucesso"}, 200
