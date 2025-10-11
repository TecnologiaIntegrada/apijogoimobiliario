# Dockerfile para FastAPI - API Jogo Imobiliário
FROM python:3.11-slim AS builder

WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir --user -r requirements.txt

# Imagem final
FROM python:3.11-slim

WORKDIR /app

# Copiar dependências instaladas
COPY --from=builder /root/.local /root/.local

# Copiar código da aplicação
COPY app/ ./app/

# Adicionar ao PATH
ENV PATH=/root/.local/bin:$PATH

# Expor porta
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/docs')" || exit 1

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

