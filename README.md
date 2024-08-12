# Sistema de Recomendação de Livros

Este projeto é um sistema de recomendação de livros construído com Flask. Ele permite que os usuários se cadastrem, respondam a perguntas para indicar suas preferências e recebam recomendações de livros. Os usuários também podem avaliar livros e adicionar novos livros ao sistema.

O sistema de recomendação da aplicação foi projetado para sugerir livros aos usuários com base em suas preferências iniciais e nas avaliações que eles fazem de livros ao longo do tempo. Vamos detalhar como esse sistema funciona, quais algoritmos são usados e como eles são aplicados na prática.

## Objetivo do Sistema de Recomendação
O objetivo principal do sistema de recomendação é sugerir livros aos usuários de acordo com seus interesses e preferências pessoais. Isso é feito em duas etapas principais:

## Recomendação Inicial

1. Quando um usuário se cadastra pela primeira vez, ele pode fornecer preferências iniciais (como gêneros ou temas de interesse). Com base nessas preferências, o sistema sugere um ou mais livros que podem ser de interesse do usuário.
Recomendações Baseadas em Avaliações:

2. À medida que o usuário avalia os livros que leu, o sistema ajusta suas recomendações futuras com base nessas avaliações. Livros que receberam boas avaliações de usuários com preferências semelhantes são recomendados.

## Algoritmos Utilizados

Dois algoritmos principais de Machine Learning são usados para implementar esse sistema de recomendação.

### Árvore de Decisão (Decision Tree) para Recomendação Inicial

A árvore de decisão é um algoritmo de aprendizado supervisionado usado para classificação e regressão. Ele funciona criando um modelo que prevê o valor de uma variável-alvo com base em várias variáveis de entrada. No contexto desta aplicação, a árvore de decisão é utilizada para classificar e sugerir um livro inicial com base nas respostas do usuário a um questionário inicial sobre suas preferências.

#### Funcionamento

* O usuário responde a algumas perguntas iniciais (por exemplo, gênero preferido, autor favorito, etc.).
* As respostas do usuário são convertidas em um vetor de características (features).
* A árvore de decisão processa esse vetor de características e seleciona o livro que melhor corresponde às preferências do usuário.

### K-Nearest Neighbors (KNN) para Recomendações Baseadas em Avaliações

K-Nearest Neighbors (KNN) é um algoritmo de aprendizado supervisionado utilizado para classificação e regressão. Ele funciona encontrando os k exemplos mais próximos no conjunto de dados e usando esses exemplos para fazer previsões. No contexto desta aplicação, o KNN é utilizado para recomendar livros com base nas avaliações que o usuário forneceu para livros anteriores.

#### Funcionamento

* Cada vez que o usuário avalia um livro, essas avaliações são registradas e armazenadas no banco de dados.
* O algoritmo KNN analisa essas avaliações e encontra usuários semelhantes (ou seja, usuários que avaliaram livros de maneira semelhante).
* Com base nas avaliações de outros usuários semelhantes, o KNN recomenda livros que esses usuários gostaram, mas que o usuário atual ainda não leu.

## Funcionalidades do sistema

- Cadastro de usuários com perguntas de preferências
- Recomendação inicial de livros usando árvore de decisão
- Avaliação de livros pelos usuários
- Adição de novos livros pelos usuários
- Recomendação baseada em avaliações dos usuários


## Fluxo do Sistema

1. Cadastro do Usuário

O usuário se cadastra no sistema e responde a um questionário inicial sobre suas preferências.
Com base nas respostas, a árvore de decisão recomenda um ou mais livros iniciais.

2. Interação Contínua

À medida que o usuário lê e avalia os livros recomendados, o sistema registra essas avaliações.
O algoritmo KNN utiliza essas avaliações para ajustar as recomendações futuras, tornando-as mais precisas e personalizadas ao longo do tempo.

3. Adição de Novos Livros

Os usuários podem adicionar novos livros ao sistema, enriquecendo o banco de dados e melhorando as recomendações para outros usuários.

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
