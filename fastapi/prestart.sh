#!/bin/sh

echo "Waiting for mysql to start..."
until mysqladmin ping --host="$MYSQL_HOST" --user="$MYSQL_USER" --password="$MYSQL_PASSWORD" --port="$MYSQL_PORT" --silent; do
    echo "Waiting for mysql to start..."
    sleep 5
done

# DB migration.
cd /db && alembic upgrade head
echo "finish DB migration."
