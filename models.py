from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Atendimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    solicitante = db.Column(db.String(100), nullable=False)
    dia_atual = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)

class Cin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pronta")
