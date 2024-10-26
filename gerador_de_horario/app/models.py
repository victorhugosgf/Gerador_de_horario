from . import db

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    aulas = db.relationship('Aula', backref='professor', lazy=True)

class Disciplina(db.Model):
    __tablename__ = 'disciplina'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)
    aulas = db.relationship('Aula', backref='disciplina', lazy=True)

class Sala(db.Model):
    __tablename__ = 'sala'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    aulas = db.relationship('Aula', backref='sala', lazy=True)

class Aula(db.Model):
    __tablename__ = 'aula'
    id = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    dia = db.Column(db.String(10), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=False)
