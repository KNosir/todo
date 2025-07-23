📝 ToDo App
A simple ToDo application built with FastAPI, SQLAlchemy, and PostgreSQL. This app allows users to create, read, update, and delete tasks.

🚀 Features
Create new todos

List all todos

Mark todos as active or completed

Soft delete support (optional)

RESTful API with JSON responses

⚙️ Tech Stack
FastAPI — Web framework

PostgreSQL — Database

SQLAlchemy (Async) — ORM

Alembic — DB migrations

📦 Installation
bash
Копировать код
git clone https://github.com/knosir/todo.git
cd todo-app
uv venv install  # or: pip install -r requirements.txt
🧪 API Endpoints
Method	Endpoint	Description
GET	/todos	Get all todos
POST	/todos	Create new todo
GET	/todos/{id}	Get todo by ID
PUT	/todos/{id}	Update todo
DELETE	/todos/{id}	Delete todo

📁 Project Structure
pgsql
Копировать код
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── controllers/
│       └── todo.py
├── alembic/
│   └── versions/
└── README.md
