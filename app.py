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

# Rotas

@app.route('/alunos', methods=['GET'])
def getAluno():
    r = dados['alunos']
    return jsonify(r)

@app.route('professores', methods=['GET'])
def getProfessores():
    r = dados['professores']
    return jsonify(r)

@app.route('/turmas', methods=['GET'])
def getTurmas():
    r = dados['turmas']
    return jsonify(r)

#

if __name__ == '__main__':
    app.run(debug=True)