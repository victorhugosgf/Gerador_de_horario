from flask import jsonify, request
from . import db
from .models import Professor, Disciplina, Sala, Aula
from . import create_app

app = create_app()

@app.route('/professores', methods=['GET'])
def get_professores():
    professores = Professor.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome, 'email': p.email} for p in professores])

@app.route('/professores', methods=['POST'])
def add_professor():
    data = request.json
    novo_professor = Professor(nome=data['nome'], email=data['email'])
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({'id': novo_professor.id}), 201

