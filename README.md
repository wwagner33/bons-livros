# Sistema de Recomendação de Livros

Este projeto é um sistema de recomendação de livros construído com Flask. Ele permite que os usuários se cadastrem, respondam a perguntas para indicar suas preferências e recebam recomendações de livros. Os usuários também podem avaliar livros e adicionar novos livros ao sistema.

## Funcionalidades

- Cadastro de usuários com perguntas de preferências
- Recomendação inicial de livros usando árvore de decisão
- Avaliação de livros pelos usuários
- Adição de novos livros pelos usuários
- Recomendação baseada em avaliações dos usuários

## Tecnologias

- Flask
- SQLAlchemy
- pandas
- scikit-learn
- PostgreSQL

## Configuração

1. Clone o repositório:
    ```
    git clone https://github.com/seu-usuario/recomendador_livros.git
    cd recomendador_livros
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Configure o banco de dados PostgreSQL no `config.py`.

4. Execute as migrações do banco de dados:
    ```
    flask db init
    flask db migrate -m "Migração inicial."
    flask db upgrade
    ```

5. Carregue os dados do dataset:
    ```
    python scripts/carregar_livros.py
    ```

6. Inicie o servidor:
    ```
    flask run
    ```

7. Acesse o sistema no navegador em `http://127.0.0.1:5000`.



### Introdução aos Sistemas de Recomendação

**Definição:** Sistemas de recomendação são algoritmos que sugerem itens aos usuários com base em diversos critérios. Eles são amplamente usados para melhorar a experiência do usuário, aumentar o engajamento e as vendas.

### Tipos de Sistemas de Recomendação

1. **Filtragem Colaborativa:**
   - **Usuário-usuário:** Sugere itens que usuários semelhantes gostaram.
   - **Item-item:** Sugere itens similares aos que o usuário já gostou.

2. **Filtragem Baseada em Conteúdo:**
   - Recomenda itens similares àqueles que o usuário já visualizou, baseado em características dos itens (gênero, autor, etc.).

3. **Filtragem Híbrida:**
   - Combina métodos colaborativos e baseados em conteúdo para melhorar a precisão das recomendações.

### Técnicas Comuns

1. **Modelos Baseados em Matriz de Fatoração:**
   - Ex.: SVD (Singular Value Decomposition), que decompõe a matriz de interações em fatores latentes.

2. **Modelos Baseados em Redes Neurais:**
   - Usam deep learning para capturar complexidades nas interações usuário-item.

3. **Modelos Baseados em K-Nearest Neighbors (KNN):**
   - Usa proximidade para recomendar itens similares aos preferidos pelo usuário.

### Implementação Básica

Para começar com um sistema de recomendação simples, podemos usar bibliotecas como `Surprise` ou `TensorFlow` em Python. Aqui está um exemplo básico usando `Surprise`:

```python
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

# Carregando dados de exemplo
data = Dataset.load_builtin('ml-100k')

# Definindo o algoritmo
algo = SVD()

# Avaliando o desempenho usando cross-validation
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
```

### Aplicações Práticas

1. **Netflix:** Usa uma combinação de filtragem colaborativa e modelos de aprendizado profundo.
2. **Amazon:** Combina filtragem colaborativa, baseada em conteúdo e algoritmos de associação.
3. **Spotify:** Utiliza redes neurais para analisar a música e recomendar novas faixas.

### Desafios

1. **Cold Start:** Dificuldade em recomendar para novos usuários ou itens.
2. **Escalabilidade:** Manter desempenho com grandes volumes de dados.
3. **Privacidade:** Balancear personalização com a proteção de dados dos usuários.

### Referências

- **"Recommender Systems Handbook"**: Uma referência abrangente sobre o tema.
- **Coursera e Udemy:** Cursos sobre sistemas de recomendação com implementação prática.
- **Artigos do IEEE:** Publicações científicas com as últimas novidades na área.

Se precisar de mais detalhes ou de uma implementação específica, me avise!

## Licença

Este projeto está licenciado sob a Licença GPLv3.
