#!/bin/bash

# This script installs the required dependencies and downloads the scispacy model
# Run this before deploying to Streamlit Cloud

# Update pip
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install scispacy model
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz

echo "Setup complete!"