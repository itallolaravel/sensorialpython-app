from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados (Substitua pelos dados do seu banco)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.gfxabtythrcxoyykzcxi:ammOQUq63B76Ss34@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Necessário para o uso de flash messages

db = SQLAlchemy(app)

# Definir o modelo para o atendimento
class Atendimento(db.Model):
    __tablename__ = 'atendimentos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    solicitante = db.Column(db.String(100), nullable=False)
    
    def __init__(self, nome, cpf, email, solicitante):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.solicitante = solicitante

# Criação do banco de dados
with app.app_context():
    db.create_all()

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_atendimento():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        solicitante = request.form['solicitante']
        
        # Verificar se o CPF já está cadastrado
        atendimento_existente = Atendimento.query.filter_by(cpf=cpf).first()
        if atendimento_existente:
            flash('Erro: CPF já cadastrado.', 'error')
            return redirect(url_for('cadastrar_atendimento'))
        
        # Criar um novo atendimento
        try:
            novo_atendimento = Atendimento(nome, cpf, email, solicitante)
            db.session.add(novo_atendimento)
            db.session.commit()
            flash('Atendimento cadastrado com sucesso!', 'success')
            return redirect(url_for('cadastrar_atendimento'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar atendimento: {str(e)}', 'error')
            return redirect(url_for('cadastrar_atendimento'))

    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)