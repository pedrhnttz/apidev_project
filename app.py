from config import app, db
from aluno.alunos_route import alunos_bp
from professor.professores_route import professores_bp
from turma.turmas_route import turmas_bp

app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )