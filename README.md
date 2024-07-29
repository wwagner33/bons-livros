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

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT.
