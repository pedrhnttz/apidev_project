dados = {
    'turmas': [
        {
            'id': 0,
            'nome': 'ADS 3B Noite',
            'materia': 'Análise e Desenvolvimento de Sistemas',
            'descricao': None,
            'ativo': None,
            'professor_id': None
        }
    ]
}

IdTurma = 0

# Funções de rota

def get_turmas():
    return dados['turmas']

def get_turma_by_id(turma_id):
    turmas = dados['turmas']
    for turma in turmas:
        if turma.get('id') == turma_id:
            return turma
    raise Exception('Turma não encontrada')

def create_turma(turma):
    
    turma['nome'] = create_nome(turma)
    turma['materia'] = create_materia(turma.get('materia'))

    turma['id'] = create_id(turma.get('id'))

    turma['descricao'] = turma.get('descricao', None)
    turma['ativo'] = bool(turma.get('ativo', None))
    turma['professo_id'] = int(turma.get('professor_id', None))

    dados['turmas'].append(turma)
    return {'msg': 'Turma criada!'}

def update_turma(turma_id, turma_up):
    turma = get_turma_by_id(turma_id)

    turma_up['nome'] = create_nome(turma_up)
    turma_up['materia'] = create_materia(turma_up.get('materia'))

    turma_up['descricao'] = turma_up.get('descricao', None)
    turma_up['ativo'] = bool(turma_up.get('ativo', None))
    turma_up['professo_id'] = int(turma_up.get('professor_id', None))

    turma.update(turma_up)
    return {'msg': 'Turma atualizada!'}

def delete_turma(turma_id):

    turmas = dados['turmas']
    turma = get_turma_by_id(turma_id)

    turmas.remove(turma)

    if turma not in turmas:
        return {'msg': 'Turma deletada!'}
    raise Exception('Não foi possível deletar a turma')

# Funções de lógica

def create_nome(turma):
    if not turma or 'nome' not in turma:
        raise Exception('Turma/Nome inválido')
    nome = turma.get('nome')
    return nome

def create_materia(materia):
    if not materia:
        raise Exception('Materia Invalida')
    return materia

def create_id(turma_id):
    global IdTurma
    turmas = dados['turmas']
    if turma_id:
        for turma in turmas:
            if turma['id'] == turma_id:
                raise Exception('Este ID já está sendo utilizado')
        return turma_id
    else:
        IdTurma += 1
        return IdTurma