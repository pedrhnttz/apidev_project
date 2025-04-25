from datetime import datetime

dados = {
    'professores': [
        {
            'id': 0,
            'nome': 'Caio',
            'materia': 'Desenvolvimento de APIs E Microsserviços',
            'obs': 'Especialista em Microsserviços'
        }
    ]
}

IdProfessor = 0

# Classes de exceções

class ProfessorNotFound(Exception):
    def __init__(self):
        super().__init__({'Professor não encontrado'})

class ProfessorInvalid(Exception):
    def __init__(self):
        super().__init__({'Professor/Nome inválido'})

# Funções de rota

def get_professores():
    return dados['professores']

def get_professor_by_id(id_professor):
    professores = dados['professores']
    for professor in professores:
        if professor.get('id') == id_professor:
            return professor
    raise ProfessorNotFound

def create_professor(professor):

    professor['nome'] = create_nome(professor)
    professor['materia'] = create_materia(professor.get('materia'))
    professor['obs'] = create_obs(professor.get('obs'))
    professor['id'] = create_id(professor.get('id', None))

    dados['professores'].append(professor)
    return {'msg': 'Professor criado!'}

def update_professor(id_professor, professor_up):
    professor = get_professor_by_id(id_professor)

    professor_up['nome'] = create_nome(professor_up)
    professor_up['materia'] = create_materia(professor_up.get('materia'))
    professor_up['obs'] = create_obs(professor_up.get('obs'))

    professor.update(professor_up)
    return {'msg': 'Professor atualizado!'}

def delete_professor(professor_id):
    professores = dados['professores']
    professor = get_professor_by_id(professor_id)

    professores.remove(professor)

    if professor not in professores:
        return {'msg': 'Professor deletado!'}
    raise Exception('Não foi possível deletar o professor')
    
# Funções de lógica

def create_nome(professor):
    if not professor or 'nome' not in professor:
        raise ProfessorInvalid
    nome = professor.get('nome')
    return nome

def create_materia(materia):
    if not materia:
        raise Exception('Matéria inválida')
    return materia

def create_obs(obs):
    if not obs:
        raise Exception('Observação inválida')
    return obs

def create_id(id_professor):
    global IdProfessor
    professores = dados['professores']
    if id_professor:
        for professor in professores:
            if professor['id'] == id_professor:
                raise Exception('Este ID já está sendo utilizado')
        return id_professor
    else:
        IdProfessor += 1
        return IdProfessor