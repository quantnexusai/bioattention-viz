import subprocess
import sys
import os
import importlib

# Function to check if the model is installed
def is_model_installed():
    try:
        # Try to import the module
        import en_core_sci_sm
        return True
    except ImportError:
        return False

# Function to install the model
def install_model():
    print("Installing scispacy model...")
    model_url = "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz"
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", model_url])
        print("Model installed successfully")
        # Force Python to recognize the newly installed package
        importlib.invalidate_caches()
        return True
    except Exception as e:
        print(f"Failed to install model: {e}")
        return False

# Run this when this file is imported
if not is_model_installed():
    install_model()