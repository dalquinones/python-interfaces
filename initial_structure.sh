#!/bin/bash

# Crear carpetas para organizar el proyecto
mkdir data interfaces models utils

# Crear archivos vacíos en cada carpeta
touch data/        # Archivo del modelo (se llenará al entrenar)
touch interfaces/gradio_app.py       # Código para la interfaz en Gradio
touch interfaces/streamlit_app.py    # Código para la interfaz en Streamlit
touch models/entrenar_modelo.py      # Script para entrenar y guardar el modelo
touch utils/preprocess.py            # Funciones de preprocesamiento de imágenes
touch README.md                      # Descripción general del proyecto


echo "Creando ambiente virtual ..."
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

echo "Instalando librerias ..."
# Instalación de dependencias
pip install -r requirements.txt


# Agregar mensaje de éxito
echo "Estructura de proyecto creada exitosamente en el directorio."

#chmod +x initial_structure.sh
#./initial_structure.sh
