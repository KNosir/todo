FROM python:3.11-slim

# 1. Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl gcc libpq-dev build-essential git libffi-dev python3-pip

# 2. Устанавливаем uv напрямую через pip (из PyPI)
RUN pip install uv

# 3. Устанавливаем рабочую директорию
WORKDIR /app

# 4. Копируем pyproject.toml (для кеша)
COPY pyproject.toml ./

# 5. Устанавливаем зависимости через uv в системную среду
RUN uv pip install --system .

# 6. Копируем остальной код
COPY . .

# 7. Открываем порт
EXPOSE 8000

# 8. Запускаем приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
