import pandas as pd
from sqlalchemy import create_engine

# Caminho local para o arquivo .zip
livros_url = './dataset/BX-Books-Dump.zip'

# Carregar os dados
livros = pd.read_csv(livros_url, compression='zip', sep=';', on_bad_lines='skip', encoding='latin-1', low_memory=False)

# Limpar e preparar os dados
livros.columns = ['ISBN', 'Titulo', 'Autor', 'Ano_Publicacao', 'Editora', 'Imagem_URL_S', 'Imagem_URL_M', 'Imagem_URL_L']
livros = livros[['ISBN', 'Titulo', 'Autor', 'Ano_Publicacao', 'Editora']]

# Conectar ao banco de dados e inserir os dados
engine = create_engine('postgresql://usuario:senha@localhost:5432/meubanco')
livros.to_sql('livro', engine, if_exists='replace', index=False)
