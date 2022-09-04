#!/usr/bin/env bash
set -e

#waiting for postgres
echo host: $POSTGRES_HOST
echo port: $POSTGRES_PORT
until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT
do
  echo "Waiting for PostgreSQL to accept connection ..."
  sleep 1
done

echo "Postgres is ready, running the migrations..."

# Apply database migrations
echo "Apply database migrations ..."
python manage.py migrate

# Start server
echo "Starting server ..."
python manage.py runserver 0.0.0.0:8000