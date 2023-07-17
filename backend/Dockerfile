# Usa una imagen base de Python con la versión que necesites
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará FastAPI
EXPOSE 8000
