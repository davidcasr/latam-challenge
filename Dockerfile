# Usa una imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto 8080
EXPOSE 8080

# Ejecuta el servidor de FastAPI
CMD ["python", "challenge/api.py"]
