# 🎬 Flix API

**Flix API** é uma aplicação desenvolvida durante o curso **Django Master** da [PycodeBR](https://pycodebr.com), com o objetivo de criar uma API RESTful para gerenciamento de filmes, gêneros, atores e avaliações, utilizando autenticação JWT.

---

## 🚀 Tecnologias

- **Python** 3.10+
- **Django**
- **Django REST Framework**
- **SQLite** (podendo ser trocado por PostgreSQL)
- **Django Admin**
- **Django REST Simple JWT**
- **Docker** (opcional)

---

## 🧩 Funcionalidades

- CRUD completo para **filmes**, **gêneros**, **atores** e **avaliações**
- Estatísticas: total de filmes, média de avaliações, contagem por gênero
- Autenticação JWT: endpoints protegidos com tokens
- Interface de administração via Django Admin

---

## 📦 Instalação local

1. Clone o repositório:
   ```bash
   git clone https://github.com/Veloso-holanda/flix-api.git
   cd flix-api
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

6. Execute o servidor:
   ```bash
   python manage.py runserver
   ```
   Acesse a API em `http://127.0.0.1:8000/`

---

## 📬 Endpoints principais

### 🎥 Filmes
| Método | Rota                       | Descrição                    |
|--------|----------------------------|------------------------------|
| GET    | `/api/filmes/`             | Lista filmes                 |
| POST   | `/api/filmes/`             | Cria um novo filme           |
| GET    | `/api/filmes/{id}/`        | Detalhes de um filme         |
| PUT    | `/api/filmes/{id}/`        | Atualiza um filme existente  |
| DELETE | `/api/filmes/{id}/`        | Remove um filme              |

### 🎭 Gêneros, 👥 Atores, ⭐ Avaliações
Operações **GET / POST / GET/{{id}} / PUT/{{id}} / DELETE/{{id}}**

### 📊 Estatísticas
| Método | Rota                    | Descrição                               |
|--------|-------------------------|-----------------------------------------|
| GET    | `/api/filmes/stats/`    | Estatísticas: total, média, por gênero  |

---

## 🔐 Autenticação JWT

- **Obter tokens**:
  ```http
  POST /api/auth/token/
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```

- **Verificar token**:
  ```http
  POST /api/auth/token/verify/
  {
    "token": "seu_access_token"
  }
  ```

- **Refresh token**:
  ```http
  POST /api/auth/token/refresh/
  {
    "refresh": "seu_refresh_token"
  }
  ```

Para endpoints protegidos, inclua no header:
```
Authorization: Bearer <seu_access_token>
```

---

## ✅ Pré-requisitos

- Python 3.10+
- pip
- Ambiente virtual

---

## 👨‍💻 Autor

Desenvolvido por **Gabriel Veloso** como projeto final do curso **Django Master** da **PycodeBR**.  
Veja meu perfil no GitHub: [@Veloso-holanda](https://github.com/Veloso-holanda)

---

## 📚 Curso

Parte do curso: [Django Master — PycodeBR](https://pycodebr.com)