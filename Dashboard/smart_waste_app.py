import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image


st.set_page_config(page_title="Smart Waste Classification")

# Load model with Streamlit caching
@st.cache_resource
def load_cnn_model():
    return load_model("Models/smart_waste_sorting_model.keras")

model = load_cnn_model()
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Image preprocessing
def preprocess_image(image):
    image = image.resize((128, 128)).convert('RGB')
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Main UI
st.title("♻️ Smart Waste Classification")
st.write("Upload an image of waste to classify it as Recyclable, Compost, or Trash.")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Predict"):
        with st.spinner("Analyzing..."):
            try:
                processed = preprocess_image(image)
                prediction = model.predict(processed)[0]
                predicted_class = class_names[np.argmax(prediction)]
                confidence = float(np.max(prediction))
                
                st.success(f"Prediction: **{predicted_class.capitalize()}**")
                st.info(f"Confidence: {round(confidence * 100, 2)}%")
            except Exception as e:
                st.error(f"Error: {str(e)}")