# Projeto de Gerenciamento de Horário Escolar

Sistema de gerenciamento de horário escolar desenvolvido em Python usando o framework Flask e o MySQL como banco de dados. Ele permite gerenciar professores, disciplinas, salas e aulas de forma eficiente.

## Funcionalidades

- **Professores**: Adicionar, atualizar, listar e remover professores.
- **Disciplinas**: Adicionar, atualizar, listar e remover disciplinas.
- **Salas**: Adicionar, atualizar, listar e remover salas.
- **Aulas**: Adicionar, atualizar, listar e remover aulas, incluindo informações de professor, disciplina, dia, hora e sala.

## Tecnologias Utilizadas

- **Python** com **Flask**: Framework para desenvolvimento web.
- **MySQL**: Banco de dados para armazenar as informações.
- **SQLAlchemy**: ORM para manipulação do banco de dados.
- **Flask-RESTful**: Para a criação de APIs RESTful.

## Pré-requisitos

- **Python** 3.11
- **MySQL** Server
- **pip** para instalação de pacotes Python

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/victorhugosgf/Gerador_de_horario
   cd seu-repositorio

2. python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. Instale as dependencias 
    pip install Flask-SQLAlchemy
    pip install pymysql
    pip install fastapi uvicorn
    pip install -r requirements.txt

4. Configure o arquivo de configuração do banco de dados (config.py)
    Crie um banco de dados no MySQL chamado mydb (ou o nome que preferir).
    Atualize as credenciais de banco de dados no código (app.config['SQLALCHEMY_DATABASE_URI']).

    5. Inicie o Servidor
    python run.py

Esse `README.md` ajudará a documentar o projeto para futuros colaboradores e usuários. 





