from flask import Flask, flash, request ,jsonify, render_template
from werkzeug.utils import secure_filename
from ML_APP import image_predict
import json
import cv2
import os
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/') 
def main():
  return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST']) 
def upload_file():
  if request.method == 'POST':
    if 'file' not in request.files:
        flash('No file part')
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return 'No selected file'
       
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],    
                                filename))
        img = 'static/uploads/'+filename
        label = image_predict(img)
        return render_template('upload.html',label=label,filename = '/uploads/'+filename)
  return render_template('upload.html')
if __name__ == '__main  __':
    app.debug = True
    app.run()
