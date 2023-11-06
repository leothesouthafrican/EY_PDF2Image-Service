#!/bin/bash

# Define the directory structure
DIRSTRUCTURE="pdf-to-image-service/app pdf-to-image-service"

# Create directories
for dir in $DIRSTRUCTURE; do
  mkdir -p $dir
done

# Create files
touch pdf-to-image-service/app/__init__.py
touch pdf-to-image-service/app/main.py
touch pdf-to-image-service/Dockerfile
touch pdf-to-image-service/requirements.txt
touch pdf-to-image-service/README.md

echo "File structure successfully created."
