from flask import Blueprint, jsonify, request # type: ignore

turmas_bp = Blueprint('turmas', __name__)

dados = {
    'turmas': [
        {
            'id': 1,
            'turma_id': 12,
            'descricao': 'ADS 3B',
            'ativa': True,
            'professor_id': 123
        }
    ]
}

@turmas_bp.route('/turmas', methods=['GET'])
def getTurma():
    return jsonify(dados['turmas'])

@turmas_bp.route('/turmas', methods=['POST'])
def criandoTurma():
    response = request.get_json()
    turma = dados['turmas']

    response['id'] = len(turma) + 1

    turma.append(response)
    return jsonify(response),200

@turmas_bp.route('/turmas/<int:idTurma>', methods=['GET'])
def getTurmaId(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:
            return jsonify(turma)
    return jsonify({'mensagem':'Turma não encontrada'}), 400

@turmas_bp.route('/turmas/<int:idTurma>', methods=['PUT'])
def atualizandoTurmas(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:
            response = request.get_json()
            if not response or 'nome' not in response:
                return jsonify({'erro': 'turma sem nome'}), 400
            turma['nome'] = response['nome']
            return jsonify(response), 200
    return jsonify({'mensagem':'Turma não encontrada'}), 400 

@turmas_bp.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deletandoTurma(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma deletada'}), 200
    return jsonify({'mensagem': 'Turma não encontrada'}), 404