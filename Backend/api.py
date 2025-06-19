from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model("Models/smart_waste_sorting_model.keras")  # Updated path and extension

class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = image.resize((128, 128))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route("/predict", methods=["POST"])
def predict():
    print("Request received")
    if 'file' not in request.files:
        print("No file part")
        return jsonify({"error": "No file provided"}), 400

    image_file = request.files['file']
    if image_file.filename == '':
        print("Empty filename")
        return jsonify({"error": "No selected file"}), 400

    try:
        image_bytes = image_file.read()
        processed = preprocess_image(image_bytes)
        prediction = model.predict(processed)[0]
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))

        return jsonify({
            "predicted_class": predicted_class,
            "confidence": round(confidence, 4)
        })
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
