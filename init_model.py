import subprocess
import sys
import importlib

def install_scispacy_model():
    try:
        importlib.import_module("en_core_sci_sm")
    except ImportError:
        print("Installing biomedical model. This may take a few minutes...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz"])
        importlib.import_module("en_core_sci_sm")

if __name__ == "__main__":
    install_scispacy_model()