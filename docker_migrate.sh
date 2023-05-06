#!/bin/bash

# Check if migrations exist
if python manage.py makemigrations --dry-run | grep "No changes detected"; then
  echo "No Django migrations detected."
else
  echo "Django migrations detected. Running migrations..."
  python manage.py migrate
fi