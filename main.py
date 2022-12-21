from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

#==================================================================================================
#variavel de referencia ao flask 
app = Flask(__name__)

# encriptar o passwords do usuário
app.secret_key = '123'

#string conexao
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'postgresql',
    usuario = "clinic-sys",
    senha = "123456",
    servidor = "localhost:5435",
    database = "postgres"
)

#==================================================================================================
db = SQLAlchemy(app)

class Admin(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    position = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
    
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./components/home.html')

@app.route('/register')
def registerAdmin():
    return render_template('./components/register.html')

@app.route('/create-admin', methods=['POST'])
def createAdmin():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    cpf = request.form['cpf']
    position = request.form['position']
    
    newAdmin = Admin( name = name,
                     password = password,
                     email = email,
                     cpf = cpf,
                     position = position
                     )
    
    db.session.add(newAdmin)
    
    db.session.commit()
     
    return redirect(url_for('login_page'))
    

@app.route('/new_patient')
def new_patient_page():
    return render_template('./components/newPatient.html', titulo='Cadastro de Paciente')


@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    email = request.form['email']
    cpf = request.form['cpf']

    #variavel nova recebendo classe jogo e filtrando pelo nome
    #person = Person.query.filter_by(name=name).first()
    # if condicional recebendo a variavel caso exista jogos cadastrados 
    #if person:
    #    flash('Cadastro Já Existe!')
    #    return redirect(url_for('home_page'))

    #variavel criada recebendo variaveis e as variaveis refente ao form
    new_person = Person(name=name, email=email, cpf=cpf)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(new_person)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    #redirecionando para lista de pessoas
    return redirect(url_for('list_page'))

@app.route('/list')
def list_page():
    list = Person.query.order_by(Person.id)
    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("./components/list.html", titulo = 'Lista de Pacientes', person = list)

@app.route('/more_info/<id_patient>')
def more_info(id_patient):
    return render_template('./components/moreInfoPatient.html', patient=id_patient)

@app.route('/login')
def login_page():
    proximo = request.args.get('proximo')

    return render_template('./components/login.html', proximo=proximo)
#a
@app.route('/editPatient/<int:id>')
def edit_patient(id):
    #if 'admin_logado' not in session or session['admin_logado'] is None:
    #   return redirect(url_for('login_page', proximo= url_for('edit_patient')))
    #fazer uma query do banco
    person = Person.query.filter_by(id=id).first()
    return render_template('./components/editPatient.html', titulo= 'Editar Cadastro', person = person)

@app.route('/update', methods=['POST'])
def update():
    
    person = Person.query.filter_by(id=request.form['id']).first()
    
    person.name = request.form['name']
    person.email = request.form['email']
    person.cpf = request.form['cpf']

    db.session.add(person)
    db.session.commit()
    return redirect(url_for('home_page'))

@app.route('/delete/<int:id>')
def delete(id):
    #if 'usuario_logado' not in session or session['usuario_logado'] is None:
    #    return redirect(url_for('login_page'))

    Person.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Cadastro deletado com sucesso')
    return redirect(url_for('list_page'))

@app.route('/authentication', methods=['POST',])
def authentication():
    admin = Admin.query.filter_by(email=request.form['email']).first()
    if admin:
        
        if request.form['password'] == admin.password:

            session['usuario_logado'] = admin.email
            

            flash(admin.name + ' - Logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)
        
        else:
            flash('usuario ou senha incorretos tente novamente')
            return redirect(url_for('login_page'))

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login_page'))

if __name__ == '__main__' :
    app.run(debug=True)