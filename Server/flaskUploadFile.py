import os
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
from clothing_identification import captureAnalyzeClothing
app = Flask(__name__)

UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, template_folder='../GUI')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'test'

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        file_path = UPLOAD_FOLDER + secure_filename(f.filename)
        session['upload_file_path'] = file_path
        f.save(UPLOAD_FOLDER + secure_filename(f.filename))
        outObj = captureAnalyzeClothing(file_path)
        outString = outObj["text"]
        return render_template('output-image.html', image_path = outObj["out_path"], alt_text = outString)



if __name__ == '__main__':
   app.run(debug = True)