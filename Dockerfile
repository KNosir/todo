FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

# Run Alembic migrations if needed (optional)
# RUN alembic upgrade head

# Start FastAPI app (assuming app.main contains your FastAPI `app`)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
