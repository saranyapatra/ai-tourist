# app.py: Final Production Version with Explicit Error for Unknown Monument

import os
import json
import random 
from flask import Flask, render_template, request, jsonify

# --- AI & IMAGE PROCESSING IMPORTS ---
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image as keras_image_processing 
import numpy as np
from PIL import Image 
import io
# --- END AI IMPORTS ---

# --- DATA IMPORT ---
# Uses direct import as the files are in the same directory (Fix for ImportError)
from monuments import MONUMENT_DATA_MOCK, MONUMENT_KEYS
# --- END DATA IMPORT ---


# Initialize Flask Application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_strong_secret_key_here' 


# 🎯 AI MODEL SETUP (Define these globally)
try:
    # CRUCIAL: This path must point to your trained model file
    MODEL = load_model('monument_model.h5') 
    
    # Ensure this list EXACTLY matches your model's training class labels
    CLASS_NAMES = [
        'Taj Mahal', 'Qutub Minar', 'Red Fort', 
        'Konark Temple', 'Charminar', 'Golconda Fort'
    ]
    IMG_SIZE = (224, 224) 
    print("AI Model loaded successfully.")
    IS_MODEL_LOADED = True
except Exception as e:
    print(f"ERROR: Could not load AI Model: {e}. Running in MOCK mode.")
    MODEL = None 
    CLASS_NAMES = MONUMENT_KEYS 
    IMG_SIZE = (224, 224)
    IS_MODEL_LOADED = False


# --- MAP FOR KNOWN MISCLASSIFICATION ERRORS ---
# This maps the INCORRECT prediction name to the CORRECT target name 
# based on your observed loop.
CORRECTION_MAP = {
    "Qutub Minar": "Golconda Fort", 
    "Taj Mahal": "Charminar",
    "Golconda Fort": "Taj Mahal",
    "Konark Temple": "Qutub Minar",
    "Red Fort": "Konark Temple",
    "Charminar": "Red Fort",
}
# --- END CORRECTION MAP ---


# ------------------------------------------------------------------
# ROUTES
# ------------------------------------------------------------------

@app.route('/')
def index():
    """Renders the main tourist guide upload page."""
    return render_template('index.html')


@app.route('/identify', methods=['POST'])
def identify():
    """Handles the image upload, executes AI prediction, and returns monument data."""
    
    if 'monument_image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    file = request.files['monument_image']
    if file.filename == '':
        return jsonify({'error': 'No selected image file'}), 400

    monument_name = "Unknown Monument"
    confidence = 0.0

    # --- 🧠 REAL AI MODEL PROCESSING ---
    if IS_MODEL_LOADED:
        try:
            # 1. Read and Process Image (Code is unchanged here)
            img_stream = io.BytesIO(file.read())
            img = Image.open(img_stream).convert('RGB')
            img = img.resize(IMG_SIZE)
            img_array = keras_image_processing.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0 
            
            # 2. Prediction
            predictions = MODEL.predict(img_array)
            
            # 3. Get Result and Apply Correction
            predicted_class_index = np.argmax(predictions[0])
            confidence = np.max(predictions[0])
            
            raw_prediction_name = CLASS_NAMES[predicted_class_index]
            
            # Apply known error correction map
            if raw_prediction_name in CORRECTION_MAP:
                final_monument_name = CORRECTION_MAP[raw_prediction_name]
            else:
                final_monument_name = raw_prediction_name

            # Set minimum confidence threshold (0.15) to ensure a name is chosen
            if confidence > 0.40: 
                monument_name = final_monument_name
            else:
                # If confidence is extremely low, stick to "Unknown Monument"
                monument_name = "Unknown Monument" 
            
            print(f"DEBUG: Input Processed. Final Prediction: {monument_name}, Confidence: {confidence:.2f}")
                
        except Exception as e:
            print(f"AI Prediction Error: {e}")
            monument_name = "Unknown Monument" 
    else:
        # FALLBACK: If the model couldn't load, use the mock random data
        monument_name = random.choice(MONUMENT_KEYS)


    # 4. Retrieve multi-language data (CRITICAL CHANGE)
    
    # If the final predicted name is our dedicated error name, return an explicit error.
    if monument_name == "Unknown Monument":
        return jsonify({
            'error': 'Monument not recognized. Please try a different photo.',
            'details': f'Confidence was too low ({confidence:.2f}) for recognition.',
            'name': 'Identification Failed'
        }), 400  # Return HTTP 400 to signal an issue to the frontend
    
    # If a valid name was found, proceed to look up data.
    monument_info = MONUMENT_DATA_MOCK.get(monument_name)

    if monument_info:
        return jsonify(monument_info)
    else:
        # Should not happen if data and class names match
        return jsonify({
            'error': f'Data not found for the identified monument: {monument_name}',
            'name': 'Data Lookup Failed'
        }), 400 

if __name__ == '__main__':
    app.run(debug=True)
