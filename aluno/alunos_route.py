from flask import Blueprint, jsonify, request # type: ignore
from datetime import datetime

alunos_bp = Blueprint('alunos', __name__)

dados = {
    'alunos': [
        {
            'id': 0,
            'nome': 'Pedro',
            'idade': 21,
            'turma_id': 12,
            'data_nascimento': '26/01/2004',
            'nota_semestre_1': 10.0,
            'nota_semestre_2': 8.0,
            'media_final': 9.0
        }
    ]
}

idAluno = 1

@alunos_bp.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(dados['alunos'])

@alunos_bp.route('/alunos', methods=['POST'])
def criandoAluno():
    global idAluno
    response = request.get_json()
    if not response or 'nome' not in response:
        return jsonify({'erro': 'aluno sem nome'}), 400

    aluno = dados['alunos']

    id_aluno = response.get('id', None)
    if id_aluno:
        for a in aluno:
            if a['id'] == id_aluno:
                return jsonify({'erro': 'id ja utilizada'}), 400
        response['id'] = id_aluno
    else:
        response['id'] = idAluno
        idAluno += 1

    nota1 = float(response.get('nota_primeiro_semestre', 0))
    nota2 = float(response.get('nota_segundo_semestre', 0))
    media_final = (nota1 + nota2) / 2
    response['media_final'] = media_final

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

    aluno.append(response)
    return jsonify(response), 200

@alunos_bp.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            response = request.get_json()
            if not response or 'nome' not in response:
                return jsonify({'erro': 'aluno sem nome'}), 400
            aluno['nome'] = response['nome']
            return jsonify(aluno), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 400

@alunos_bp.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunoId(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            return jsonify(aluno)
    return jsonify({'erro': 'aluno nao encontrado'}), 400

@alunos_bp.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deletandoAluno(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno deletado'}), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 400