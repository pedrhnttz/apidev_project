from flask import Flask, jsonify, request

app = Flask(__name__)

dados = {
    'alunos':[
        {
            'id': 1,
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
            'professor_id': 123,
            'nome': 'Caio',
            'idade': 27,
            'materia': 'Dev API E Micros',
            'obs': 'Contato com aluno via Chat'
        }
    ],
    'turmas': [
        {
            'turma_id': 12,
            'descricao': 'ADS 3B',
            'ativa': True,
            'professor_id': 123
        }
    ]
}

# Classes para tratativa de exceções ###################################################################################

class AlunoNotFound(Exception):
    def _init_(self, msg='Erro, Aluno não identificado ou inexistente!'):
        self.msg = msg
        super()._init_(self.msg)

class AlunoExists(Exception):
    def _init_(self, msg='Erro, Aluno já existente!'):
        self.msg = msg
        super()._init_(self.msg)

# Funções para requisições #############################################################################################

def getAlunoById(idAluno):
    for aluno in dados['alunos']:
        if aluno['id'] == idAluno:
            return aluno
    raise AlunoNotFound()

def alunoAlreadyExists(idAluno):
    for aluno in dados['alunos']:
        if aluno['id'] == idAluno:
            return True
    return False

def delAlunoById(idAluno):
    alunos = dados['alunos']
    for indice, aluno in enumerate(alunos):
        if aluno['Id'] == idAluno:
            alunos.pop(indice)
            return {'Mensagem': 'Aluno deletado com sucesso.'}
    raise AlunoNotFound()

def chgAluno(id_aluno, nome, idade, turma_id, data_nascimento, nota_semestre_1, nota_semestre_2, media_final):
    try:
        for aluno in dados['alunos']:
            if aluno['Id'] == id_aluno:
                aluno['nome'] = nome
                aluno['idade'] = idade
                aluno['turma_id'] = turma_id
                aluno['data_nascimento'] = data_nascimento
                aluno['nota_semestre_1'] = nota_semestre_1
                aluno['nota_semestre_2'] = nota_semestre_2
                aluno['media_final'] = media_final
                return {'Detalhes': 'Aluno atualizado com sucesso!'}, 200
        raise AlunoNotFound()
    except Exception:
        return {'Erro': 'Não foi possível atualizar o aluno', 'Descrição': str(Exception)}, 500

# Rotas ################################################################################################################
# Alunos #######################################################################

@app.route('/alunos', methods=['GET'])
def getAlunosRoute():
    r = dados['alunos']
    return jsonify(r)

@app.route('/alunos/<int:idAluno>', methods=['GET'])
def getAlunoByIdRoute(idAluno):
    try:
        aluno = getAlunoById(idAluno)
        return jsonify(aluno)
    except AlunoNotFound:
        return jsonify({'Erro': str(AlunoNotFound)}), 404
    
@app.route('/alunos', methods=['POST'])
def addAlunoRoute():
    alunoNovo = request.json
    alunoNovo['id'] = int(alunoNovo['id'])
    alunoNovo['turma_id'] = int(alunoNovo['turma_id'])

    try:
        if alunoAlreadyExists(alunoNovo['Id']):
            raise AlunoExists()
        dados['alunos'].append(alunoNovo)
        return jsonify({'mensagem': 'Aluno criado com sucesso!', 'aluno': alunoNovo}), 201
    except AlunoExists:
        return jsonify({'Erro': str(AlunoExists)}), 400
    
@app.route('/alunos/deletar/<int:idAluno>', methods=['DELETE'])
def delAlunoRoute(idAluno):
    try:
        r = delAlunoById(idAluno)
        return jsonify(r), 200
    except AlunoNotFound:
        return jsonify({'Erro': str(AlunoNotFound)}), 404
    
@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def chgAlunoRoute(idAluno):
    aluno = request.json
    if not aluno:
        return jsonify({
            'Erro': 'Requisição inválida',
            'Descrição': 'O corpo da requisição está vazio, preencha todos os campos'
        }), 400
    try:
        resultado, status_code = chgAluno(
            idAluno,
            aluno.get('nome'),
            aluno.get('idade'),
            aluno.get('turma_Id'),
            aluno.get('data_nascimento'),
            aluno.get('nota_semestre_1'),
            aluno.get('nota_semestre_2'),
            aluno.get('media_final')
        )
        return jsonify(resultado), status_code
    except AlunoNotFound:
        return jsonify({'Erro': str(AlunoNotFound)}), 404
    except Exception:
        return jsonify({'Erro': 'Falha ao atualizar aluno', 'Detalhes': str(Exception)}), 500

# Professores ##################################################################

@app.route('/professores', methods=['GET'])
def getProfessores():
    r = dados['professores']
    return jsonify(r)

# Turmas #######################################################################

@app.route('/turmas', methods=['GET'])
def getTurmas():
    r = dados['turmas']
    return jsonify(r)

########################################################################################################################

if __name__ == '__main__':
    app.run(debug=True)