FROM python:3.9-slim-buster

# Install uv
RUN pip install uv

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

# Install dependencies using uv
RUN uv pip install --system --no-cache-dir -r pyproject.toml

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
