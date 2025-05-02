from flask import jsonify
from datetime import datetime,date
from config import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    data_nascimento = db.Column(db.Date, nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    disciplina = db.Column(db.String(50), nullable = False)
    salario = db.Column(db.Float, nullable = False)

    turmas = db.relationship('Turma', back_populates='professor')

    def __init__(self, nome, data_nascimento, disciplina, salario):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idade = self.calcularIdade()
        self.disciplina = disciplina
        self.salario = salario

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "data_nascimento":self.data_nascimento,
            "idade":self.idade,
            "disciplina":self.disciplina,
            "salario":self.salario
        }
    
    def calcularIdade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))



# Classes de exceções

class ProfessorNotFound(Exception):
    def __init__(self):
        super().__init__({'Professor não encontrado'})

class ProfessorInvalid(Exception):
    def __init__(self):
        super().__init__({'Professor/Nome inválido'})

# Funções de rota

def get_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def get_professor_by_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNotFound
    return professor.to_dict()


def create_professor(professor):
    if not professor or 'nome' not in professor:
        return jsonify({'erro': 'professor sem nome'}), 400

    novo_professor = Professor(
        nome = professor['nome'],
        disciplina = professor['disciplina'],
        data_nascimento = datetime.strptime(professor['data_nascimento'], "%Y-%m-%d").date(),
        salario = float(professor['salario'])
    )
    db.session.add(novo_professor)
    db.session.commit()

    return {"message": "Professor adicionado com sucesso!"}, 201

def update_professor(id_professor, professor_up):
    professor = Professor.query.get(id_professor)
    if not professor:
        return jsonify({'erro':'professor nao encontrado'})
    professor.nome = professor_up['nome']
    professor.disciplina = professor_up['disciplina']
    professor.data_nascimento = datetime.strptime(professor_up['data_nascimento'], "%Y-%m-%d").date()
    professor.salario = professor_up['salario']
    professor.idade = professor.calcularIdade()
    db.session.commit()
    return {'msg': 'professor atualizado!'}

def delete_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if not professor:
        raise Exception('Não foi possível deletar o professor')
    db.session.delete(professor)
    db.session.commit()
    return {"msg":"professor deletado"}

    
