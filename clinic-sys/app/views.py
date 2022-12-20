from flask import render_template, request, redirect, session, flash, url_for
from datetime import datetime
from app.main import db, app
from app.models import Admin,Person,Reports

@app.route('/')
def root():
    if 'admin_logado' not in session or session['admin_logado'] is None:
        #recurso querystring
        return redirect(url_for('login'))
    list = Person.query.order_by(Person.id)
    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("list.html", titulo = 'Lista de Pacientes', person = list)

#return redirect('/login')
@app.route('/new')
def new():

    if 'admin_logado' not in session or session['admin_logado'] is None:
        #recurso querystring
        return redirect(url_for('login', proximo= url_for('novo')))
    return render_template('new.html', titulo='Cadastro de Pacientes')

@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    email = request.form['email']
    cpf = request.form['cpf']
    
    
    #create description
    date = datetime.date.today()
    description = request.form['description']

    #variavel nova recebendo classe jogo e filtrando pelo nome
    person = Person.query.filter_by(name=name).first()
    
    # if condicional recebendo a variavel caso exista jogos cadastrados 
    if person:
        flash('Cadastro Já Existe!')
        return redirect(url_for('root'))

    #variavel criada recebendo variaveis e as variaveis refente ao form
    new_person = Person(name=name, email=email, cpf=cpf)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(new_person)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    
    new_report = Reports(person=person, date=date, description=description)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(new_report)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    #redirecionando para lista de pessoas
    return redirect(url_for('root'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'admin_logado' not in session or session['admin_logado'] is None:
        return redirect(url_for('login', proximo= url_for('edit')))
    #fazer uma query do banco
    person = Person.query.filter_by(id=id).first()
    return render_template('edit.html', titulo= 'Editar Cadastro', person = person)

@app.route('/update', methods=['POST',])
def update():
    
    person = Person.query.filter_by(id=request.form['id']).first()
    
    person.name = request.form['name']
    person.email = request.form['email']
    person.cpf = request.form['cpf']

    db.session.add(person)
    db.session.commit()
    return redirect(url_for('root'))

@app.route('/delete/<int:id>')
def delete(id):
    if 'admin_logado' not in session or session['admin_logado'] is None:
        return redirect(url_for('login'))

    Person.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Cadastro deletado com sucesso')
    return redirect(url_for('root'))

@app.route('/logout')
def logout():
    session['admin_logado'] = None
    flash('Voce foi desconectado')

    return redirect(url_for('login'))

@app.route('/login')
def login():

        proximo = request.args.get('proximo')

        return render_template('login.html', proximo=proximo)

@app.route('/authenticate', methods=['POST',])
def authenticate():
    admin = Admin.query.filter_by(email=request.form['admin']).first()
    if admin:
        
        if request.form['password'] == admin.password:

            session['admin_logado'] = admin.email
            

            flash(admin.name + ' - Logado com sucesso')

            proxima_pagina = request.form['proximo']

            return redirect(proxima_pagina)
        
        else:
            flash('usuario ou senha incorretos tente novamente')
            #dinamizando url

            return redirect(url_for('login'))

    else:
        flash('usuario ou senha incorretos tente novamente')
        #dinamizando url

        return redirect(url_for('login'))