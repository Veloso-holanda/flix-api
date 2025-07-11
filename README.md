# 🎬 Flix API

Este é um projeto desenvolvido durante o curso **Django Master** da [PycodeBR](https://pycodebr.com), com o objetivo de construir uma API RESTful robusta para gerenciamento de conteúdos de streaming, como filmes e séries.

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Django
- Django REST Framework
- SQLite (ou PostgreSQL)
- Django Admin
- Docker (opcional)

## 📦 Funcionalidades

- CRUD completo de categorias e conteúdos
- Endpoints protegidos com autenticação JWT
- Organização modular de apps
- Serialização e validação com DRF
- Interface de administração do Django

## 🔧 Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Veloso-holanda/flix-api.git
   cd flix-api

Crie e ative o ambiente virtual:


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Instale as dependências:


pip install -r requirements.txt
Aplique as migrações:


python manage.py migrate
Rode o servidor:

python manage.py runserver

📮 Endpoints Principais

Método	Rota	Descrição
GET	/api/filmes/	Lista todos os filmes
POST	/api/filmes/	Cria um novo filme
GET	/api/filmes/{id}/	Detalhes de um filme
PUT	/api/filmes/{id}/	Atualiza um filme existente
DELETE	/api/filmes/{id}/	Remove um filme

⚠️ É necessário autenticação para rotas protegidas.

✅ Requisitos do Projeto
Python 3.10 ou superior

pip instalado

Familiaridade com Django/DRF

👨‍💻 Autor
Desenvolvido por Gabriel Veloso como parte do curso Django Master da PycodeBR.
GitHub: @Veloso-holanda

