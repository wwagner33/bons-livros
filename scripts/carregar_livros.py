# scripts/carregar_livros.py

import pandas as pd
from sqlalchemy import create_engine

# Carregar os dados
livros_url = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'
livros = pd.read_csv(livros_url, compression='zip', sep=';', error_bad_lines=False, encoding='latin-1', low_memory=False)

# Limpar e preparar os dados
livros.columns = ['ISBN', 'Titulo', 'Autor', 'Ano_Publicacao', 'Editora', 'Imagem_URL_S', 'Imagem_URL_M', 'Imagem_URL_L']
livros = livros[['ISBN', 'Titulo', 'Autor', 'Ano_Publicacao', 'Editora']]

# Conectar ao banco de dados e inserir os dados
engine = create_engine('postgresql://usuario:senha@localhost:5432/meubanco')
livros.to_sql('livro', engine, if_exists='replace', index=False)
