from flask import Blueprint, request, jsonify

from .professores_model import get_professores, create_professor, get_professor_by_id, update_professor, delete_professor

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def getProfessores():
    return jsonify(get_professores())

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def getProfessorIdRoute(id):
    try:
        professor = get_professor_by_id(id)
        return jsonify(professor), 200
    except Exception as e:
        return jsonify({'erro': str(e)})

@professores_bp.route('/professores', methods=['POST'])
def createProfessor():
    try:
        data = request.json
        professor = create_professor(data)
        return jsonify(professor)
    except Exception as e:
        return jsonify({'erro': str(e)})

@professores_bp.route('/professores/<int:id>', methods=['PUT'])
def updateProfessor(id):
    try:
        dados_up = request.get_json()
        professor_up = update_professor(id, dados_up)
        return jsonify(professor_up), 200
    except Exception as e:
        return jsonify({'erro': str(e)})

@professores_bp.route('/professores/<int:id>', methods=['DELETE'])
def deleteProfessor(id):
    try:
        professor_rm = delete_professor(id)
        return jsonify(professor_rm)
    except Exception as e:
        return jsonify({'erro': str(e)})