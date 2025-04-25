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

# Classes de exceções

class AlunoNotFound(Exception):
    def __init__(self):
        super().__init__({'Aluno não encontrado'})

class AlunoInvalid(Exception):
    def __init__(self):
        super().__init__({'Aluno/Nome inválido'})

class IdAlreadyExists(Exception):
    def __init__(self):
        super().__init__({'Este ID já está sendo utilizado'})

class AlunoUnderage(Exception):
    def __init__(self):
        super().__init__({'Aluno não possui idade necessária'})

class AlunoDeleteError(Exception):
    def __init__(self):
        super().__init__({'Não foi possível excluir o aluno'})

# Funções de rota

def  get_alunos():
    return dados['alunos']

def get_aluno_by_id(id_aluno):
    alunos = dados['alunos']
    for aluno in alunos:
        if aluno.get('id') == id_aluno:
            return aluno
    raise AlunoNotFound

def create_aluno(aluno):

    aluno['nome'] = create_nome(aluno)
    aluno['id'] = create_id(aluno.get('id', None))
    aluno['nota_primeiro_semestre'] = float(aluno.get('nota_primeiro_semestre', 0))
    aluno['nota_segundo_semestre'] = float(aluno.get('nota_segundo_semestre', 0))
    aluno['media_final'] = create_media_final(aluno['nota_primeiro_semestre'], aluno['nota_segundo_semestre'])
    aluno['turma_id'] = float(aluno.get('turma_id', 0))

    aluno['data_nascimento'] = aluno.get('data_nascimento', None)
    aluno['idade'] = create_idade(aluno['data_nascimento'])

    dados['alunos'].append(aluno)
    return {'msg': 'Aluno criado!'}

def update_aluno(aluno_id, aluno_up):
    aluno = get_aluno_by_id(aluno_id)

    aluno_up['nome'] = create_nome(aluno_up)
    aluno_up['nota_primeiro_semestre'] = float(aluno_up.get('nota_primeiro_semestre', 0))
    aluno_up['nota_segundo_semestre'] = float(aluno_up.get('nota_segundo_semestre', 0))
    aluno_up['media_final'] = create_media_final(aluno_up['nota_primeiro_semestre'], aluno_up['nota_segundo_semestre'])
    aluno_up['turma_id'] = float(aluno_up.get('turma_id', 0))

    aluno_up['data_nascimento'] = aluno_up.get('data_nascimento', None)
    aluno_up['idade'] = create_idade(aluno_up['data_nascimento'])

    aluno.update(aluno_up)
    return {'msg': 'Aluno atualizado!'}
    

def delete_aluno(aluno_id):
    alunos = dados['alunos']
    aluno = get_aluno_by_id(aluno_id)

    alunos.remove(aluno)

    if aluno not in alunos:
        return {'msg': 'Aluno deletado!'}
    raise AlunoDeleteError

# Funções de lógica

def create_nome(aluno):
    if not aluno or 'nome' not in aluno:
        raise AlunoInvalid
    nome = aluno.get('nome')
    return nome

def create_id(id_aluno):
    global idAluno
    alunos = dados['alunos']
    if id_aluno:
        for a in alunos:
            if a['id'] == id_aluno:
                raise IdAlreadyExists
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
            if idade >= 18:
                return idade
            raise AlunoUnderage
        except ValueError:
            return None
    else:
        return None
