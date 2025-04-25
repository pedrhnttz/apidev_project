from flask import Blueprint, request, jsonify

from .alunos_model import get_alunos, get_aluno_by_id, create_aluno, update_aluno, delete_aluno, AlunoNotFound

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(get_alunos())

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def getAlunoById(id):
    try:
        aluno = get_aluno_by_id(id)
        return jsonify(aluno), 200
    except AlunoNotFound as e:
        return jsonify({'erro': str(e)}), 404

@alunos_bp.route('/alunos', methods=['POST'])
def createAluno():
    try:
        data = request.json
        aluno = create_aluno(data)
        return jsonify(aluno)
    except Exception as e:
        return jsonify({'erro': str(e)})

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def updateAluno(id):
    try:
        dados_up = request.get_json()
        aluno_up = update_aluno(id, dados_up)
        return jsonify(aluno_up), 200
    except Exception as e:
        return jsonify({'erro': str(e)})

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deleteAluno(id):
    try:
        aluno_rm = delete_aluno(id)
        return jsonify(aluno_rm)
    except Exception as e:
        return jsonify({'erro': str(e)})