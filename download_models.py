import subprocess
import sys

def download_scispacy_model():
    print("Downloading scispacy model...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz"])

if __name__ == "__main__":
    download_scispacy_model()