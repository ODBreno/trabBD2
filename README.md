
<p align="center">

<p align="center">
    <a href="https://www.python.org/">
        <img align="center" alt="Python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg">
    </a>
</p>

# Script de carga para API da Câmara dos Deputados

Script em python formulado para realizar a carga no banco de dados relacional com PostgreSQL e utilizando ORM SQLAlchemy.

---
## Sobre

Conforme as orientações para realização da parte 1 do trabalho da disciplina de Banco de Dados II da Universidade Federal de Itajubá, a equipe desenvolveu um script responsável por realizar a carga nas tabelas do banco.

As orientações estão divididas nos seguintes tópicos:

- [Script de carga para API da Câmara dos Deputados](#script-de-carga-para-api-da-camara-dos-deputados)
  - [Sobre](#sobre)
  - [Banco de dados :chair: :game\_die:](#banco-de-dados-chair-game_die)
  - [Pré-requisitos e configuração :hammer\_and\_wrench:](#pré-requisitos-e-configuração-hammer_and_wrench)
  - [Tecnologias :technologist:](#tecnologias-technologist)
  - [Contribuidores](#contribuidores)

---
## Banco de dados :chair: :game_die:

Para realizar a conexão com o banco utilizou-se:
>PostgreSQL - 15.2

>PGadmin4 - 7.2

>SQLAlchemy - 1.4.48

---
## Pré-requisitos e configuração :hammer_and_wrench:
No geral, para executar a aplicação é recomendado que o sistema já possua:

    > Python 3.11

Para executar esse script é necessário:

```bash

# Criar o banco com nome trabalho_bd2 para realizar a carga

# Clone este repositório com
$ git clone git@github.com:ODBreno/trabalho_banco_de_dados_2.git
# OU
$ git clone https://github.com/ODBreno/trabalho_banco_de_dados_2.git

# Navegue até o diretório clonado com terminal

# Abra script no Vscode ou editor de preferência
$ code .

# No DAO, mude as credenciais de acesso do banco (lembre-se de criar um banco com o nome IGDB pelo SGDB)
$ engine = create_engine("postgresql+psycopg2://seu_user:sua_senha@localhost:5432/trabalho_bd2")

# Rode o script pelo terminal
$ py controller.py
# OU
$ python3 controller.py

# Há ums ordem correta identificada no menu para popular elas!

```
---
## Tecnologias :technologist:
    O ponto de início deste projeto foi um ambiente Python, as dependências utilizadas estão descritas abaixo: 
---
Dependências:

    -> Python 3.11
    - SQLAlchemy 2.3
    - psycopg2 2.9.6
    - sqlacodegen 3.0.0rc2
---
Banco de Dados:

    -> PostgreSQL
    - pgAdmin4 7.0
    - BRmodelo
---
Utilitários:

    -> Dev
    - Visual Studio Code 1.78
---  

## Contribuidores

<table>
  <tr>
</td>
    <td align="center"><a href="https://github.com/ODBreno"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/92598517?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Breno Oliveira Dias</b></sub></a><br /><a href="https://github.com/ODBreno" title="Breno">:technologist:</a></td>
    <td align="center"><a href="https://github.com/perebati"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63824184?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Batista Pereira</b></sub></a><br /><a href="https://github.com/perebati" title="Lucas">🧑‍🎓:technologist:</a></td>
    <td align="center"><a href="https://github.com/danielhfc"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/51706879?s=400&u=75f461cf2aed84e32eda2adb2f65f7c9363e82ba&v=4" width="100px;" alt=""/><br /><sub><b>Daniel Henrique Ferreira Carvalho</b></sub></a><br /><a href="https://github.com/danielhfc" title="Daniel">🤵‍♂️</a></td>
     <td align="center"><a href="https://github.com/NathaliaStilpen"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/81316348?v=4" width="100px;" alt=""/><br /><sub><b>Nathalia Stilpen</b></sub></a><br /><a href="https://github.com/NathaliaStilpen" title="Nathalia">🤵‍♂️</a></td>
</td>
  </tr>
</table>
