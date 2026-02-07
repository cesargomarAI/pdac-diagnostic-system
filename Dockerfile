# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
COPY . .

# Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto que usa Streamlit
EXPOSE 8501

# Comando para arrancar la app al encender el contenedor
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
