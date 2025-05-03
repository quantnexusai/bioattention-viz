import subprocess
import sys
import importlib

def install_scispacy_model():
    model_url = "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz"
    model_name = "en_core_sci_sm"

    try:
        importlib.import_module(model_name)
    except ImportError:
        print("Installing biomedical model. This may take a few minutes...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", model_url],
                check=True,
                stdout=subprocess.DEVNULL,  # or use subprocess.PIPE for logs
                stderr=subprocess.DEVNULL
            )
            importlib.import_module(model_name)
            print(f"{model_name} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {model_name}. Error code: {e.returncode}")
        except ImportError:
            print(f"{model_name} still not available after installation.")

if __name__ == "__main__":
    install_scispacy_model()
