import sys
import subprocess
from interfaces.gradio_app import app as gradio_app

# Estrategia para seleccionar la interfaz
class InterfazStrategy:
    def ejecutar(self):
        pass

class GradioStrategy(InterfazStrategy):
    def ejecutar(self):
        # Llamar directamente a la función `launch()` de Gradio
        print("Ejecutando interfaz de Gradio...")
        gradio_app.launch()

class StreamlitStrategy(InterfazStrategy):
    def ejecutar(self):
        # Ejecutar el comando `streamlit run` desde el script
        print("Ejecutando interfaz de Streamlit...")
        subprocess.run(["streamlit", "run", "interfaces/streamlit_app.py"])

class InterfazContext:
    def __init__(self, strategy: InterfazStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: InterfazStrategy):
        self._strategy = strategy

    def ejecutar_interfaz(self):
        self._strategy.ejecutar()

def main():
    # Pedir al usuario que elija la interfaz
    print("Seleccione la interfaz a ejecutar:")
    print("1. Gradio")
    print("2. Streamlit")
    
    opcion = input("Opción (1 o 2): ")

    if opcion == "1":
        # Usar la estrategia Gradio
        contexto = InterfazContext(GradioStrategy())
    elif opcion == "2":
        # Usar la estrategia Streamlit
        contexto = InterfazContext(StreamlitStrategy())
    else:
        print("Opción no válida.")
        return

    # Ejecutar la interfaz seleccionada
    contexto.ejecutar_interfaz()

if __name__ == "__main__":
    main()
