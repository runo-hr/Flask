from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
import io
from hub import app
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/work')
def work_page():
    return render_template('work.html')

@app.route('/profile')
def profile_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/pneumonia_overview')
def pneumonia_overview_page():
    return render_template('pneumonia_overview.html')

@app.route('/model_creation')
def model_creation_page():
    return render_template('model_creation.html')

@app.route('/application')
def application_page():
    return render_template('application.html')

@app.route('/tech_stack')
def stack_page():
    return render_template('tech_stack.html')

'''
@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'Normal': prediction[0][0],
            'Pneumonia': prediction[0][1]
        }
    }
    return jsonify(response)
'''

