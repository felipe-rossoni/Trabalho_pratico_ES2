# Imagem base leve de Python
FROM python:3.9-slim

# Define diretório de trabalho
WORKDIR /app

# Copia dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte
COPY . .

# Expõe a porta do serviço
EXPOSE 8100

# Comando de inicialização
CMD ["python", "app.py"]