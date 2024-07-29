# utils.py

from modelos import Livro, Avaliacao
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

def recomendacao_inicial(preferencias):
    # Simulação de preferências e dados de livros
    livros = Livro.query.all()
    X = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    y = [livro.titulo for livro in livros]
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    return clf.predict([preferencias])[0]

def recomendacao_baseada_em_avaliacoes(usuario_id):
    avaliacoes = Avaliacao.query.filter_by(usuario_id=usuario_id).all()
    livros = Livro.query.all()
    if not avaliacoes:
        return livros
    X = [[avaliacao.livro_id, avaliacao.nota] for avaliacao in avaliacoes]
    y = [livro.id for livro in livros]
    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(X, y)
    recomendacoes = model.predict(X)
    return [Livro.query.get(int(rec)) for rec in recomendacoes]
