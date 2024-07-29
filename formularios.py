# formularios.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange

class FormularioRegistro(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Registrar')

class FormularioLivro(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    titulo = StringField('Título', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    ano_publicacao = IntegerField('Ano de Publicação', validators=[DataRequired()])
    editora = StringField('Editora', validators=[DataRequired()])
    submit = SubmitField('Adicionar Livro')

class FormularioAvaliacao(FlaskForm):
    nota = SelectField('Nota', choices=[(i, i) for i in range(6)], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Avaliar')
