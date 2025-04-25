from flask import Blueprint, request

from .professores_model import getProfessor, criandoProfessor, getProfessorId, atualizandoProfessor, deletandoProfessor

professores_bp = Blueprint('professores', __name__)

idProfessor = 1

@professores_bp.route('/professores', methods=['GET'])
def getProfessorRoute():
    return getProfessor()

@professores_bp.route('/professores', methods=['POST'])
def criandoProfessorRoute():
    response = request.get_json()
    return criandoProfessor(response)

@professores_bp.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessorIdRoute(idProfessor):
    return getProfessorId(idProfessor)

@professores_bp.route('/professores/<int:idProfessor>', methods=['PUT'])
def atualizandoProfessorRoute(idProfessor, response):
    response = request.get_json()
    return atualizandoProfessor(idProfessor, response)

@professores_bp.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deletandoProfessorRoute(idProfessor):
    return deletandoProfessor(idProfessor)