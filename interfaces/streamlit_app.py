import streamlit as st
import pickle
from preprocess import preprocess_image
from PIL import Image

# Cargar el modelo
with open("./data/modelo_digits.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Predicción de Dígitos con Streamlit")
st.write("Sube una imagen de un dígito (8x8) para hacer una predicción.")

uploaded_image = st.file_uploader("Elige una imagen...", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Imagen cargada", use_column_width=True)
    prediction = model.predict(preprocess_image(image))[0]
    st.write(f"Predicción del modelo: {prediction}")
