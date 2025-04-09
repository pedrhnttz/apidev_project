from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

dados = {
    'alunos': [
        {
            'id': 0,
            'nome': 'Pedro',
            'idade': 21,
            'turma_id': 1,
            'data_nascimento': '26/01/2004',
            'nota_semestre_1': 10.0,
            'nota_semestre_2': 8.0,
            'media_final': 9.0
        }
    ],
    'professores': [
        {
            'id': 1,
            'nome': 'Caio',
            'idade': 27,
            'materia': 'Dev API E Micros',
            'obs': 'Contato com aluno via Chat'
        }
    ],
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

idAluno = 1
idProfessor = 1

## ROTAS #######################################################################
## ALUNO #######################################################################

@app.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(dados['alunos'])

@app.route('/reseta', methods=['POST', 'DELETE'])
def reseta():
    dados['alunos'] = []
    dados['professores'] = []
    return jsonify({'mensagem': 'Dados resetados'}), 200

@app.route('/alunos', methods=['POST'])
def criandoAluno():
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
        global idAluno
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


@app.route('/alunos/<int:idAluno>', methods=['PUT'])
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


@app.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunoId(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            return jsonify(aluno)
    return jsonify({'erro': 'aluno nao encontrado'}), 400


@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deletandoAluno(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno deletado'}), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 400


## PROFESSOR ###################################################################

@app.route('/professores', methods=['GET'])
def getProfessor():
    return jsonify(dados['professores'])

@app.route('/professores', methods=['POST'])
def criandoProfessor():
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
        global idProfessor
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

@app.route('/professores/<int:idProfessor>', methods=['GET'])
def getProfessorId(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:
            return jsonify(professor)
    return jsonify({'erro': 'professor nao encontrado'}), 400

@app.route('/professores/<int:idProfessor>', methods=['PUT'])
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

@app.route('/professores/<int:idProfessor>', methods=['DELETE'])
def deletandoProfessor(idProfessor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == idProfessor:  # Use get()
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor deletado'}), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400

## TURMA #######################################################################

@app.route('/turmas', methods=['GET'])
def getTurma():
    return jsonify(dados['turmas'])


@app.route('/turmas', methods=['POST'])
def criandoTurma():
    response = request.get_json()
    turma = dados['turmas']

    response['id'] = len(turma) + 1 #start from 1

    turma.append(response)
    return jsonify(response),200 #Just return the new object

@app.route('/turmas/<int:idTurma>', methods=['GET'])
def getTurmaId(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma: #Use get()
            return jsonify(turma)
    return jsonify({'mensagem':'Turma não encontrada'}), 400 #Add status code

@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def atualizandoTurmas(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma: #Use get()
            response = request.get_json()
            if not response or 'nome' not in response:
                return jsonify({'erro': 'turma sem nome'}), 400
            turma['nome'] = response['nome']
            return jsonify(response), 200
    return jsonify({'mensagem':'Turma não encontrada'}), 400 #Add status code

@app.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deletandoTurma(idTurma):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == idTurma:  # Use get()
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma deletada'}), 200
    return jsonify({'mensagem': 'Turma não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)