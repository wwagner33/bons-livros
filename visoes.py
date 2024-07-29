from flask import render_template, flash, redirect, url_for, request
from app import app, db
from modelos import Livro, Usuario, Avaliacao
from formularios import FormularioRegistro, FormularioLivro, FormularioAvaliacao
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from utils import recomendacao_inicial, recomendacao_baseada_em_avaliacoes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livros')
def lista_livros():
    livros = Livro.query.all()
    return render_template('lista_livros.html', livros=livros)

@app.route('/livro/<int:id>', methods=['GET', 'POST'])
def detalhe_livro(id):
    livro = Livro.query.get_or_404(id)
    form = FormularioAvaliacao()
    if form.validate_on_submit():
        avaliacao = Avaliacao(nota=form.nota.data, usuario_id=current_user.id, livro_id=livro.id)
        db.session.add(avaliacao)
        db.session.commit()
        flash('Avaliação registrada com sucesso!')
        return redirect(url_for('detalhe_livro', id=livro.id))
    return render_template('detalhe_livro.html', livro=livro, form=form)

@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    form = FormularioLivro()
    if form.validate_on_submit():
        livro = Livro(
            isbn=form.isbn.data,
            titulo=form.titulo.data,
            autor=form.autor.data,
            ano_publicacao=form.ano_publicacao.data,
            editora=form.editora.data
        )
        db.session.add(livro)
        db.session.commit()
        flash('Livro adicionado com sucesso!')
        return redirect(url_for('lista_livros'))
    return render_template('adicionar_livro.html', form=form)
