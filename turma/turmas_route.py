from flask import Blueprint, request, jsonify

from .turmas_model import get_turmas, get_turma_by_id, create_turma, update_turma, delete_turma

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def getTurmaRoute():
    return jsonify(get_turmas())

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def getTurmaIdRoute(id):
    try:
        turma = get_turma_by_id(id)
        return jsonify(turma)
    except Exception as e:
        return jsonify({'erro': str(e)})

@turmas_bp.route('/turmas', methods=['POST'])
def criandoTurmaRoute():
    pass

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizandoTurmasRoute(id):
    pass

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deletandoTurmaRoute(id):
    pass