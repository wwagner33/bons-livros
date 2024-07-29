# modelos.py

from app import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=False)
    editora = db.Column(db.String(255), nullable=False)
    avaliacoes = db.relationship('Avaliacao', backref='livro', lazy=True)

    def __repr__(self):
        return f'<Livro {self.titulo}>'

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    avaliacoes = db.relationship('Avaliacao', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nome}>'

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    nota = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Avaliacao {self.nota}>'
