from setuptools import setup, find_packages

setup(
    name="bioattention-viz",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch==2.0.1",
        "transformers==4.30.2",
        "streamlit==1.27.2",
        "plotly==5.15.0",
        "numpy==1.23.5",
        "pandas==1.5.3",
        "requests==2.31.0"
    ],
)
