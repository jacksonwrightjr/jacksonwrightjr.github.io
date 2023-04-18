import cv2
from flask_cors import CORS
from clothing_identification import captureAnalyzeClothing

from flask import Flask, render_template
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    clothingMatchString = captureAnalyzeClothing(cam)
    return clothingMatchString

if __name__ == '__main__':
    # initialize the camera
    cam = cv2.VideoCapture(0)

    app.run(debug=True, port=8001)
     