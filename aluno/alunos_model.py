from datetime import date, datetime
from flask import jsonify
from config import db

#Tabela Aluno

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    data_nascimento = db.Column(db.Date, nullable = False)
    nota_semestre_1 = db.Column(db.Float, nullable = False)
    nota_semestre_2 = db.Column(db.Float, nullable = False)
    media_final = db.Column(db.Float, nullable = False)

    turma_id = db.Column(db.Integer, nullable = False)

    def __init__(self,nome,turma_id,data_nascimento,nota_semestre_1,nota_semestre_2):
        self.nome = nome
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_semestre_1 = nota_semestre_1
        self.nota_semestre_2 = nota_semestre_2
        self.idade = self.calcularIdade()
        self.media_final = self.calcularMedia()
    
    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "idade":self.idade,
            "turma_id":self.turma_id,
            "data_nascimento":self.data_nascimento,
            "nota_semestre_1":self.nota_semestre_1,
            "nota_semestre_2":self.nota_semestre_2,
            "media_final":self.media_final,

        }
    
    def calcularIdade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
    
    def calcularMedia(self):
        media = (self.nota_semestre_1 + self.nota_semestre_2) / 2
        return media


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
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def get_aluno_by_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno:
        return aluno.to_dict()
    raise AlunoNotFound

def create_aluno(aluno):
    if not aluno or 'nome' not in aluno:
        return jsonify({'erro': 'aluno sem nome'}), 400
    novo_aluno = Aluno(
        nome = aluno['nome'], 
        turma_id = int(aluno['turma_id']), 
        data_nascimento = datetime.strptime(aluno['data_nascimento'], "%Y-%m-%d").date(),
        nota_semestre_1 = aluno['nota_semestre_1'],
        nota_semestre_2 = aluno['nota_semestre_2']
        )
    db.session.add(novo_aluno)
    db.session.commit()

    return {"message": "Aluno adicionado com sucesso!"}, 201

def update_aluno(aluno_id, responseUpdate):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        pass
    aluno.nome = responseUpdate['nome']
    aluno.turma_id = responseUpdate['turma_id']
    aluno.data_nascimento = responseUpdate['data_nascimento']
    aluno.nota_semestre_1 = responseUpdate['nota_semestre_1']
    aluno.nota_semestre_2 = responseUpdate['nota_semestre_2']
    aluno.media_final = aluno.calcularMedia()
    aluno.idade = aluno.calcularIdade()
    db.session.commit()
    return {'msg': 'Aluno atualizado!'}
    

def delete_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        raise AlunoDeleteError
    db.session.delete(aluno)
    db.session.commit()
    return {"msg":"aluno deletado"}

