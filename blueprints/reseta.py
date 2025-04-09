from flask import Blueprint, jsonify # type: ignore
from blueprints.alunos import dados as alunos_data
from blueprints.professores import dados as professores_data

reseta_bp = Blueprint('reseta', __name__)

@reseta_bp.route('/reseta', methods=['POST', 'DELETE'])
def reseta():
    alunos_data['alunos'] = []
    professores_data['professores'] = []
    return jsonify({'mensagem': 'Dados resetados'}), 200