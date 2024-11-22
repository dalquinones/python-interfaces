import numpy as np

def preprocess_image(image):
    """Convierte la imagen a escala de grises, redimensiona a 8x8 y normaliza."""
    image = image.convert("L").resize((8, 8))
    image_array = np.array(image) / 16.0  # Normalización para que coincida con el dataset original
    return image_array.reshape(1, -1)
