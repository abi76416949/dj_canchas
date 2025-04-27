# Imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los requirements primero para aprovechar el cache
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd


# Copiamos el resto del proyecto
COPY . .

# Exponer el puerto (Django usa por defecto el 8000)
EXPOSE 8000

# Comando por defecto para levantar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
