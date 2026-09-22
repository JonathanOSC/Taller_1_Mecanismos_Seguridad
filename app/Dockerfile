FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#crear usuario no privilegiado
RUN useradd -m appuser

#Healthcheck
HEALTHCHECK --interval=30s --timeout=3s CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/')" || exit 1




USER appuser


CMD ["python3", "-m", "http.server", "8080"]
