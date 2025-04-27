from config import db
class Turma(db.Model):
    __tablename__ = "turmas"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)
    materia = db.Column(db.String(100), nullable = False)
    descricao = db.Column(db.String(100), nullable = False)
    ativo = db.Column(db.Integer, nullable = False)
    professor_id = db.Column(db.Integer, nullable = False)

    def __init__(self, id, nome, materia, descricao, ativo, professor_id):
        self.id = id
        self.nome = nome
        self.materia = materia
        self.descricao = descricao
        self.ativo = ativo
        self.professor_id = professor_id
    
    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "materia":self.materia,
            "descricao":self.descricao,
            "ativo":self.ativo,
            "professor_id":self.professor_id
        }
        
class TurmaNotFound(Exception):
    def __init__(self):
        super().__init__({'Turma não encontrado'})

class TurmaInvalid(Exception):
    def __init__(self):
        super().__init__({'Turma/Nome inválido'})

# Funções de rota

def getTurma():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]


def get_turma_by_id(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise Exception('Turma não encontrada')
    return turma.to_dict() 

def create_turma(turma):
    nova_turma = Turma(
        nome = turma['nome'],
        materia = turma['materia'],
        descricao = turma['descricao'],
        ativo = turma['ativo'],
        professor_id = turma['professor_id']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return {'msg': 'Turma criada!'}

def update_turma(turma_id, turma_up):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise Exception('Turma não encontrada')
    turma.nome = turma_up['nome']
    turma.materia = turma_up['materia']
    turma.descricao = turma_up['descricao']
    turma.ativo = turma_up['ativo']
    turma.professor_id = turma_up['professor_id']
    return {'msg': 'Turma atualizada!'}

def delete_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if not turma:
        raise Exception('Não foi possível deletar a turma')
    db.session.delete(turma)
    db.session.commit()

