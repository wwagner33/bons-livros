#!/bin/bash

# Create backend directories
mkdir -p backend/routes
mkdir -p backend/models
mkdir -p backend/utils

# Prompt for backend choice
echo "Select your backend technology:"
echo "1) Python (Flask)"
echo "2) Node.js (Express)"
read -p "Enter 1 or 2: " backend_choice

if [ "$backend_choice" == "1" ]; then
  # Using Python backend
  touch backend/app.py
  touch backend/requirements.txt
  touch backend/routes/auth_routes.py
  touch backend/routes/recommendation_routes.py
  touch backend/models/recommendation_model.py
  touch backend/utils/data_preprocessing.py
  touch backend/config.py
elif [ "$backend_choice" == "2" ]; then
  # Using Node.js backend
  touch backend/server.js
  touch backend/package.json
  touch backend/routes/auth_routes.js
  touch backend/routes/recommendation_routes.js
  touch backend/models/recommendation_model.js
  touch backend/utils/data_preprocessing.js
  touch backend/config.js
else
  echo "Invalid choice. Exiting script."
  exit 1
fi

# Create frontend directories
mkdir -p frontend/public
mkdir -p frontend/src/components

# Create frontend files
touch frontend/src/App.js
touch frontend/src/index.js
touch frontend/package.json

# Create data directories
mkdir -p data/raw
mkdir -p data/processed

# Create data files
touch data/raw/dataset.csv
touch data/processed/processed_dataset.csv

# Create database directory
mkdir -p database

# Create database file
touch database/schema.sql

# Create root files
touch README.md
touch .gitignore

echo "Project directory and file structure created successfully."
