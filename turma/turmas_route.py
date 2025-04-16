from flask import Blueprint, request
from turmas_model import getTurma, criandoTurma, getTurmaId, atualizandoTurmas, deletandoTurma

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def getTurmaRoute():
    return getTurma()

@turmas_bp.route('/turmas', methods=['POST'])
def criandoTurmaRoute():
    response = request.get_json()
    return criandoTurma(response)

@turmas_bp.route('/turmas/<int:idTurma>', methods=['GET'])
def getTurmaIdRoute(idTurma):
    return getTurmaId(idTurma)

@turmas_bp.route('/turmas/<int:idTurma>', methods=['PUT'])
def atualizandoTurmasRoute(idTurma):
    respose = request.get_json()
    return atualizandoTurmas(idTurma, respose)

@turmas_bp.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deletandoTurmaRoute(idTurma):
    return deletandoTurma(idTurma)