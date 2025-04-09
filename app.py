from flask import Flask, jsonify

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
            'nome': "Caio",
            'idade': 27,
            'materia': "Dev API E Micros",
            'obs': "Contato com aluno via Chat"
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

# Classes para tratativa de exceções

class AlunoNotFound(Exception):
    def _init_(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super()._init_(self.msg)

# Funções para requisições

def getAlunoById(id_aluno):
    for aluno in dados['alunos']:
        if aluno['id'] == id_aluno:
            return aluno
    raise AlunoNotFound()

# Rotas /alunos

@app.route('/alunos', methods=['GET'])
def getAlunos():
    r = dados['alunos']
    return jsonify(r)

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def getAlunoByIdRoute(id_aluno):
    try:
        aluno = getAlunoById(id_aluno)
        return jsonify(aluno)
    except AlunoNotFound:
        return jsonify({"Erro": str(AlunoNotFound)}), 404

# Rotas /professores

@app.route('/professores', methods=['GET'])
def getProfessores():
    r = dados['professores']
    return jsonify(r)

# Rotas /turmas

@app.route('/turmas', methods=['GET'])
def getTurmas():
    r = dados['turmas']
    return jsonify(r)

#

if __name__ == '__main__':
    app.run(debug=True)