from flask import Blueprint, jsonify, request # type: ignore
from datetime import datetime

professores_bp = Blueprint('professores', __name__)

dados = {
    'professores': [
        {
            'id': 1,
            'nome': 'Caio',
            'idade': 27,
            'materia': 'Desenvolvimento de APIs E Microsserviços',
            'obs': None
        }
    ]
}

idProfessor = 1

@professores_bp.route('/professores', methods=['GET'])
def getProfessor():
    return jsonify(dados['professores'])

@professores_bp.route('/professores', methods=['POST'])
def criandoProfessor():
    global idProfessor
    response = request.get_json()
    if not response or 'nome' not in response:
        return jsonify({'erro': 'professor sem nome'}), 400
    professor = dados['professores']

    id_professor = response.get('id', None)
    if id_professor:
        for a in professor:
            if a['id'] == id_professor:
                return jsonify({'erro': 'id ja utilizada'}), 400
        response['id'] = id_professor
    else:
        response['id'] = idProfessor
        idProfessor += 1

    data = response.get('data_nascimento', None)
    if data:
        try:
            data_nasc = datetime.strptime(data, '%d/%m/%Y')
            data_atual = datetime.today()
            idade = data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
            response['idade'] = idade
        except ValueError:
            response['idade'] = None
    else:
        response['idade'] = None

    professor.append(response)
    return jsonify(response), 200

@professores_bp.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessorId(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:
            return jsonify(professor)
    return jsonify({'erro': 'professor nao encontrado'}), 400

@professores_bp.route('/professores/<int:idProfessor>', methods=['PUT'])
def atualizandoProfessor(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:
            response = request.get_json()
            if not response or 'nome' not in response:
                return jsonify({'erro': 'professor sem nome'}), 400
            professor['nome'] = response['nome']
            return jsonify(response), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400

@professores_bp.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deletandoProfessor(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:  # Use get()
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor deletado'}), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400