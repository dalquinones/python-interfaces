import subprocess
import sys

# Script para ejecutar Streamlit
def run_streamlit():
    subprocess.run([sys.executable, "-m", "streamlit", "run", "interfaces/streamlit_app.py"])

if __name__ == "__main__":
    run_streamlit()