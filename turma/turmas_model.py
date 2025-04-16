from flask import jsonify, request

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

def getTurma():
    return jsonify(dados['turmas'])

def criandoTurma(response):
    turma = dados['turmas']
    response['id'] = len(turma) + 1
    turma.append(response)
    return jsonify(response),200

def getTurmaId(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:
            return jsonify(turma)
    return jsonify({'mensagem':'Turma não encontrada'}), 400

def atualizandoTurmas(idTurma, response):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:
            if not response or 'nome' not in response:
                return jsonify({'erro': 'turma sem nome'}), 400
            turma['nome'] = response['nome']
            return jsonify(response), 200
    return jsonify({'mensagem':'Turma não encontrada'}), 400 

def deletandoTurma(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma deletada'}), 200
    return jsonify({'mensagem': 'Turma não encontrada'}), 404