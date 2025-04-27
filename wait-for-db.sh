#!/bin/sh

# Esperar que la base de datos esté lista
echo "⏳ Esperando que la base de datos esté disponible..."

while ! nc -z "$1" "$2"; do
  sleep 1
done

echo "✅ Postgres levantado - continuando ejecución..."
