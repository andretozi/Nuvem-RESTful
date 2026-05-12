# Exercicio 9.4 - API RESTful na Nuvem (Azure)

Este repositorio contem a resolucao do Exercicio 9.4 da disciplina de Engenharia de Software. O objetivo principal desta atividade e o desenvolvimento de uma API RESTful utilizando o framework Flask, a gestao do codigo-fonte via GitHub e a implementacao de um pipeline de deploy automatico (CI/CD) para o Microsoft Azure.

---

## Descricao do Projeto

A aplicacao consiste em um sistema de gestao de itens (CRUD) que opera em memoria. A API foi desenhada para retornar dados estritamente no formato JSON, permitindo a interoperabilidade com diferentes clientes.

**Identificacao do Autor:**
* **Nome:** Andre Tozi
* **RA (ID):** 10436460

---

## Detalhes Tecnicos e Infraestrutura

A infraestrutura foi configurada seguindo os seguintes parametros:

* **Backend:** Python com o microframework Flask.
* **Servidor de Aplicacao:** Azure App Service (Linux) utilizando o plano F1 (Free).
* **Deploy:** Automatizado via GitHub Actions / Deployment Center, onde cada "push" para a branch principal dispara uma nova atualizacao automática no servidor de producao.
* **Testes:** Realizados atraves do Postman para validacao de todos os verbos HTTP (GET, POST, PUT, DELETE) e codigos de status correspondentes.

---

## Entregaveis

Conforme solicitado nos requisitos da atividade, seguem os links para avaliacao:

**Link para o codigo (app.py):**
(https://github.com/andretozi/Nuvem-RESTful/blob/main/app.py)

**Link para o repositorio (Deploy automatico):**
(https://github.com/andretozi/Nuvem-RESTful)

**Link para a aplicacao online (Azure):**
(https://restfull-flask-nuvem-andre.azurewebsites.net/)

**Link para a colecao do Postman:**
(https://www.postman.com/andretozi-3039168/workspace/andr-tozi-magalhes-s-workspace/request/54718241-d91c1491-efa9-4424-bc41-30f24f26775c?action=share&creator=54718241)

---

<img width="1917" height="1040" alt="image" src="https://github.com/user-attachments/assets/0e4a2a22-4a93-4b40-b570-34ccade0a383" /></br>

<img width="1920" height="993" alt="image" src="https://github.com/user-attachments/assets/0dc1fafe-a312-4e4d-bb87-538650754bee" /></br>


## Instrucoes de Execucao Local

1. Clone o repositorio: `git clone <url-do-repositorio>`
2. Instale as dependencias: `pip install -r requirements.txt`
3. Execute o servidor: `python app.py`
4. A API estara disponivel localmente em: `http://127.0.0.1:5000`
