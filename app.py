from flask import Flask, jsonify # type: ignore
from config import app
from blueprints.alunos import alunos_bp
from blueprints.professores import professores_bp
from blueprints.turmas import turmas_bp
from blueprints.reseta import reseta_bp

app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)
app.register_blueprint(reseta_bp)

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )