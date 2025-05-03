#!/bin/bash

# Install system dependencies
sudo apt-get update
sudo apt-get install -y $(cat packages.txt)

# Create virtual environment
python3 -m venv bioattention_env

# Activate virtual environment
source bioattention_env/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Download models
python download_models.py

echo "Setup complete. Activate with: source bioattention_env/bin/activate"