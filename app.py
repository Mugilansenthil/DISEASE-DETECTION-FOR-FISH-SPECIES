from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf
import io

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Load your trained model
model = tf.keras.models.load_model('model.keras')
class_names = [
    "Bacterial Red disease",
    "Epizootic Ulcerative Syndrome",
    "Fin Rot",
    "Fish Lice",
    "Healthy",
    "White Spot"
]

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    img = Image.open(file.stream).convert("RGB").resize((256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0])) * 100
    return jsonify({'class': predicted_class, 'confidence': confidence})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)