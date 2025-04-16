from flask import Blueprint, request

from .alunos_model import getAlunos, criandoAluno, updateAluno, getAlunoId, deletandoAluno

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def getAlunosRoute():
    return getAlunos()

@alunos_bp.route('/alunos', methods=['POST'])
def criandoAlunoRoute():
    response = request.get_json()
    return criandoAluno(response)

@alunos_bp.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAlunoRoute(idAluno):
    response = request.get_json()
    return updateAluno(idAluno, response)

@alunos_bp.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunoIdRoute(idAluno):
    return getAlunoId(idAluno)

@alunos_bp.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deletandoAlunoRoute(idAluno):
    return deletandoAluno(idAluno)