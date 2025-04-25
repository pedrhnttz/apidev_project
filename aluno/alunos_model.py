from datetime import datetime

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

# Exceções

class AlunoNotFound(Exception):
    def __init__(self):
        super().__init__({'Aluno não encontrado'})

# Funções

def  get_alunos():
    return dados['alunos']

def get_aluno_by_id(idAluno):
    global dados
    for aluno in dados['alunos']:
        if aluno.get('id') == idAluno:
            return aluno
    raise AlunoNotFound

def create_aluno(response):
    global idAluno, dados
    if not response or 'nome' not in response:
        resposta = {'erro': 'aluno sem nome'}
        return resposta, 400

    aluno = dados['alunos']

    id_aluno = response.get('id', None)
    if id_aluno:
        for a in aluno:
            if a['id'] == id_aluno:
                resposta = {'erro': 'id ja utilizada'}
                return resposta, 400
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
    return response, 200

def update_aluno(idAluno, response):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            if not response or 'nome' not in response:
                resposta = {'erro': 'aluno sem nome'}
                return resposta, 400
            aluno['nome'] = response['nome']
            return aluno, 200
    resposta = {'erro': 'aluno nao encontrado'}
    return resposta, 400

def delete_aluno(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            alunos.remove(aluno)
            resposta = {'mensagem': 'Aluno deletado'}
            return resposta, 200
    resposta = {'erro': 'aluno nao encontrado'}
    return resposta, 400