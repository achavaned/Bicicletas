# Imagen base
FROM python:3.8

# Crear un directorio para nuestra aplicación
WORKDIR /app

# Copiar el archivo de dependencias y las dependencias necesarias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar todos los archivos de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8000

# Especificar el comando para iniciar la aplicación
CMD ["python", "app.py"]
