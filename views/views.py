from flask import render_template, request, redirect, session, flash, url_for
from main import db, app, Admin, Person

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        #recurso querystring
        return redirect(url_for('login'))
    lista = Pessoa.query.order_by(Pessoa.id)
    #render template acessa nosso html, variavel titulo recebendo valor e sendo acessada via html.
    return render_template("lista.html", titulo = 'Lista de Pessoas', pessoas = lista)

#return redirect('/login')
@app.route('/novo')
def novo():

    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        #recurso querystring
        return redirect(url_for('login', proximo= url_for('novo')))
    return render_template('novo.html', titulo='Cadastro de Pessoa')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    #variavel nova recebendo classe jogo e filtrando pelo nome
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    # if condicional recebendo a variavel caso exista jogos cadastrados 
    if pessoa:
        flash('Cadastro Já Existe!')
        return redirect(url_for('index'))

    #variavel criada recebendo variaveis e as variaveis refente ao form
    novo_pessoa = Pessoa(nome=nome, idade=idade, altura=altura)
    #acessando variavel db e o recurso session e adicionando dados a variavel novo jogo 
    db.session.add(novo_pessoa)
    #acessando variavel db e o recurso session e comitando dados no banco
    db.session.commit()
    #redirecionando para lista de pessoas
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo= url_for('editar')))
    #fazer uma query do banco
    pessoa = Pessoa.query.filter_by(id=id).first()
    return render_template('editar.html', titulo= 'Editar Cadastro', pessoa = pessoa)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    
    pessoa = Pessoa.query.filter_by(id=request.form['id']).first()
    
    pessoa.nome = request.form['nome']
    pessoa.idade = request.form['idade']
    pessoa.altura = request.form['altura']

    db.session.add(pessoa)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))

    Pessoa.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Cadastro deletado com sucesso')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Voce foi desconectado')

    return redirect(url_for('login'))

@app.route('/login')
def login():

        proximo = request.args.get('proximo')

        return render_template('login.html', proximo=proximo)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        
        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.nickname
            

            flash(usuario.nickname + ' - Logado com sucesso')

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