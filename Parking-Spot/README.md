# 🚗 Sistema e API de Estacionamento com Python e Django do Zero

Este repositório documenta minha participação e aprendizado prático baseado na excelente série de lives da [PycodeBr](https://www.youtube.com/@pycodebr), onde é construído do zero um **Sistema e API para Estacionamento** usando **Python** e **Django**.

O projeto visa aplicar boas práticas de desenvolvimento backend com Django, criar APIs RESTful e integrar serviços externos como envio de e-mail, WhatsApp e tarefas assíncronas.

---

## 🎥 Série de Lives (YouTube)

> 🔗 Assista gratuitamente no canal da [PycodeBr](https://www.youtube.com/@pycodebr):

- 📺 Parte 1: [Modelagem e Admin](https://youtu.be/OMkiBRGHpzE)
- 📺 Parte 2: [API, Autenticação e Design](https://youtu.be/dqEq-FyYRfk)
- 📺 Parte 3: [RQL, Swagger e Docker](https://youtu.be/Eqa7hJS0l6Y)
- 📺 Parte 4: [Celery, RabbitMQ e AutoComplete](https://youtu.be/ROdqcgrZcs8)

---

## 📌 Requisitos do Projeto

Sistema de gestão de estacionamento com painel administrativo, API RESTful, autenticação de usuários, integração com serviços externos e funcionalidades como:

- Controle de entrada e saída de veículos
- Consulta de dados por placa
- Notificações por e-mail e WhatsApp
- Autenticação JWT e filtros avançados com RQL
- Painel administrativo com Django Jazzmin
- Execução assíncrona com Celery + RabbitMQ
- Banco de dados PostgreSQL
- Documentação automática da API com Swagger

📋 Requisitos funcionais detalhados:  
👉 [Ver no Whimsical](https://whimsical.com/parking-service-SSoifu29a1MVLAmLAPMk2a)

---

## 📦 Entregas por Etapa

### 🔹 Parte 1 – Estrutura inicial
- **Modelagem de dados**: definição dos modelos de Cliente, Veículo, Vaga e Registro.
- **Admin**: customização da interface administrativa padrão.
- **Signals**: atualização automática do status das vagas com base em entrada/saída.

### 🔹 Parte 2 – Interface e API
- **Django Jazzmin**: biblioteca que estiliza o admin com dashboard e tema moderno.
- **API REST das entidades**: criação dos endpoints para CRUD básico.
- **Autenticação e permissões**: lógica de acesso por ação e objetos, com visibilidade apenas para dados do dono.
- **Linter (flake8)**: verificação de estilo e boas práticas de código.
- **Requirements.txt**: organização das dependências do projeto.

### 🔹 Parte 3 – Integrações e melhorias
- **Admin em `/admin` raiz**.
- **RQL com `django-rql`**: permite filtros avançados via query params.  
  🔗 https://django-rql.readthedocs.io/en/latest/getting_started/
- **Swagger com `drf-spectacular`**: gera documentação interativa da API.  
  🔗 https://drf-spectacular.readthedocs.io/en/latest/
- **Docker e docker-compose**: containerização completa do sistema.
- **PostgreSQL**: substituição do SQLite pelo banco PostgreSQL.

### 🔹 Parte 4 – Tarefas assíncronas e automações
- **Celery + RabbitMQ**: filas para execução assíncrona de tarefas.
- **Tasks para auto completar dados do veículo** a partir da placa.
- Integrações com:
  - **EvolutionAPI** (consulta de placas)
  - **SMTP** (envio de e-mails)

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Django**: framework web robusto, escalável e com ORM poderoso.
- **Django REST Framework (DRF)**: criação de APIs RESTful com suporte a autenticação, filtros, validações e viewsets.
- **Django Jazzmin**: tema moderno para o painel admin do Django.
- **Celery**: tarefas assíncronas e agendamento.
- **RabbitMQ**: broker de mensagens utilizado pelo Celery.
- **PostgreSQL**: banco de dados relacional avançado e open source.
- **drf-spectacular**: documentação de APIs com suporte OpenAPI/Swagger.
- **django-rql**: filtros avançados baseados em Query Language REST.
- **flake8**: ferramenta de linting para manter o código limpo e padronizado.
- **Docker**: containerização de aplicações.
- **docker-compose**: orquestração dos serviços do projeto.

---

## 🙌 Agradecimentos

Um agradecimento especial ao canal [**PycodeBr**](https://www.youtube.com/@pycodebr) pela série de lives **extremamente didática e gratuita**, com conteúdo de alta qualidade para a comunidade Python/Django.

Confira os cursos oferecidos pela PycodeBr:

- 🐍 Django Master → https://pycodebr.com.br/pylive039  
- 🔗 Integration Master → https://pycodebr.com.br/integration-p...  
- 🤖 IA Master → https://pycodebr.com.br/ia-pylive039  
- 📚 Materiais e projetos → https://pycodebr.com.br/materiais-pylive  

---

## 🚧 Status

Este projeto está em andamento. Pretendo aplicar e adaptar os conhecimentos adquiridos em novos módulos, testando variações e funcionalidades mais avançadas.

