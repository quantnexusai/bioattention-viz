"""
This script downloads the scispacy model.
Run this script directly before deploying to Streamlit:
python download_models.py
"""

import subprocess
import sys

def main():
    """Download the scispacy model."""
    print("Downloading scispacy model...")
    model_url = "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz"
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", model_url])
        print("Model downloaded successfully!")
    except Exception as e:
        print(f"Error downloading model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()