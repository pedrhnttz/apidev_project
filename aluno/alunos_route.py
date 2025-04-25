from flask import Blueprint, request, jsonify

from .alunos_model import get_alunos, get_aluno_by_id, create_aluno, update_aluno, delete_aluno, AlunoNotFound

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(get_alunos())

@alunos_bp.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunoById(idAluno):
    try:
        aluno = get_aluno_by_id(idAluno)
        return jsonify(aluno), 200
    except AlunoNotFound as e:
        return jsonify({'erro': str(e)}), 404

@alunos_bp.route('/alunos', methods=['POST'])
def createAluno():
    try:
        data = request.json
        create_aluno(data)
        return jsonify(data)
    except Exception as e:
        return jsonify({'erro': str(e)})

@alunos_bp.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    response = request.get_json()
    return jsonify(update_aluno(idAluno, response))

@alunos_bp.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deleteAluno(idAluno):
    return jsonify(delete_aluno(idAluno))