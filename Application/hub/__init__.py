from flask import Flask, render_template
from tensorflow.keras.models import load_model

app = Flask(__name__)
#print(" * Loading Keras model...")
#model = load_model('vgg16-blncd-15.h5')
#print(" * Model loaded!")

from hub import routes