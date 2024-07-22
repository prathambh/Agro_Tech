from flask import Blueprint, render_template, request
import numpy as np
import joblib
import os
from app.crop import predict_crop  # Adjust the import path based on your project structure
from app.pest import pred_pest
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename  # Add this line to import secure_filename
import os
main_bp = Blueprint('main', __name__)
    
@main_bp.route('/')
def index():
    welcome_message = "Welcome to Agro Tech - Your One-Stop Solution for Agricultural Technology "
    return render_template('index.html' ,welcome_message = welcome_message )

@main_bp.route('/crop_recommendation', methods=['GET', 'POST'])
def crop_recommendation():
    return render_template('crop_recommendation.html')

@main_bp.route('/pest_detection', methods=['GET', 'POST'])
def pest_detection():
    return render_template('pest_detection.html')

@main_bp.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['image']
        
        # If the user does not select a file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join('static', 'user uploaded', filename)
            file.save(file_path)
            
            # Now you can proceed with your prediction logic
            pred = pred_pest(file_path)

            if pred == 'x':
                return render_template('base.html')
            elif pred in range(10):  # Assuming pred is an integer between 0 and 9
                pests = ['aphids', 'armyworm', 'beetle', 'bollworm', 'earthworm',
                         'grasshopper', 'mites', 'mosquito', 'sawfly', 'stem borer']
                pest_identified = pests[pred]
                return render_template(f'{pest_identified}.html', pred=pest_identified)
            else:
                flash('Error in pest prediction')
                return render_template('error.html')

    return render_template('error.html')  # Handle other cases if needed
        
@main_bp.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    return render_template('contact_us.html')

@main_bp.route('/aphids', methods=['GET', 'POST'])
def aphids():
    return render_template('sawfly.html')

@main_bp.route('/crop_prediction', methods=['POST'])
def crop_prediction():
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potassium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = predict_crop(data)
        final_prediction = my_prediction
        return render_template('crop-result.html', prediction=final_prediction, pred='img/crop/'+final_prediction+'.jpg')

