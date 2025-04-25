from datetime import datetime

dados = {
    'alunos': [
        {
            'id': 0,
            'nome': 'Pedro',
            'idade': 21,
            'turma_id': 12,
            'data_nascimento': '26/01/2004',
            'nota_primeiro_semestre': 10.0,
            'nota_segundo_semestre': 8.0,
            'media_final': 9.0
        }
    ]
}

idAluno = 0

# Exceções

class AlunoNotFound(Exception):
    def __init__(self):
        super().__init__({'Aluno não encontrado'})

# Funções de rota

def  get_alunos():
    return dados['alunos']

def get_aluno_by_id(idAluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            return aluno
    raise AlunoNotFound

def create_aluno(aluno):

    if not aluno or 'nome' not in aluno: # Validar nome
        raise Exception('Aluno/Nome inválido')

    aluno['id'] = create_id(aluno)
    aluno['nota_primeiro_semestre'] = float(aluno.get('nota_primeiro_semestre', 0))
    aluno['nota_segundo_semestre'] = float(aluno.get('nota_segundo_semestre', 0))
    aluno['media_final'] = create_media_final(aluno['nota_primeiro_semestre'], aluno['nota_segundo_semestre'])
    aluno['turma_id'] = float(aluno.get('turma_id', 0))

    aluno['data_nascimento'] = aluno.get('data_nascimento', None)
    aluno['idade'] = create_idade(aluno['data_nascimento'])

    dados['alunos'].append(aluno)

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

# Funções secundárias

def create_id(aluno):
    global idAluno
    alunos = dados['alunos']
    id_aluno = aluno.get('id', None)
    if id_aluno:
        for a in alunos:
            if a['id'] == id_aluno:
                raise Exception('Este ID já está sendo utilizado')
        return id_aluno
    else:
        idAluno += 1
        return idAluno
    
def create_media_final(n1, n2):
    media = (n1 + n2) / 2
    media_format = f"{media:.1f}"
    return media_format

def create_idade(data_nascimento):
    if data_nascimento:
        try:
            data_nasc = datetime.strptime(data_nascimento, '%d/%m/%Y')
            data_atual = datetime.today()
            idade = int(data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day)))
            return idade
        except ValueError:
            return None
    else:
        return None
