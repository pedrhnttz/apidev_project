from flask import Blueprint, request, jsonify

from .turmas_model import get_turmas, get_turma_by_id, create_turma, update_turma, delete_turma

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def getTurma():
    return jsonify(get_turmas())

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def getTurmaById(id):
    try:
        turma = get_turma_by_id(id)
        return jsonify(turma)
    except Exception as e:
        return jsonify({'erro': str(e)})

@turmas_bp.route('/turmas', methods=['POST'])
def createTurma():
    try:
        data = request.json
        turma = create_turma(data)
        return jsonify(turma)
    except Exception as e:
        return jsonify({'erro': str(e)})

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def updateTurma(id):
    try:
        dados_up = request.get_json()
        turma_up = update_turma(id, dados_up)
        return jsonify(turma_up), 200
    except Exception as e:
        return jsonify({'erro': str(e)})

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def deleteTurma(id):
    try:
        turma_rm = delete_turma(id)
        return jsonify(turma_rm)
    except Exception as e:
        return jsonify({'erro': str(e)})