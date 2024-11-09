# Usa una imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en la raíz del proyecto
WORKDIR /app

# Copia todo el contenido del proyecto al contenedor
COPY . /app

# Configura el PYTHONPATH para incluir el directorio de trabajo
ENV PYTHONPATH="/app"

# Instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto 8080
EXPOSE 8080

# Ejecuta el servidor de FastAPI
CMD ["python", "challenge/api.py"]
