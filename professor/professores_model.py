from datetime import datetime

dados = {
    'professores': [
        {
            'id': 1,
            'nome': 'Caio',
            'materia': 'Desenvolvimento de APIs E Microsserviços',
            'obs': 'Especialista em Microsserviços'
        }
    ]
}

# Classes de exceções



# Funções de rota

def get_professores():
    return dados['professores']

def criandoProfessor(response):
    global idProfessor
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

def getProfessorId(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:
            return jsonify(professor)
    return jsonify({'erro': 'professor nao encontrado'}), 400

def atualizandoProfessor(idProfessor, response):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:
            if not response or 'nome' not in response:
                return jsonify({'erro': 'professor sem nome'}), 400
            professor['nome'] = response['nome']
            return jsonify(response), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400

def deletandoProfessor(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:  # Use get()
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor deletado'}), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400