import gradio as gr
import pickle
from preprocess import preprocess_image

# Cargar el modelo
with open("./data/modelo_digits.pkl", "rb") as file:
    model = pickle.load(file)

def predict_digit(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)[0]
    return f"Predicción del modelo: {prediction}"

# Configuración de Gradio
app = gr.Interface(
    fn=predict_digit,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Predicción de Dígitos con Gradio"
)

if __name__ == "__main__":
    app.launch()
