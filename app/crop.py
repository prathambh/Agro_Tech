# crop.py
import numpy as np
import joblib
import os

def predict_crop(input_data):
    """
    Predict the crop based on the input data.

    Parameters:
    input_data (numpy array): A numpy array with the shape (1, 7) containing the following features:
                              [N, P, K, temperature, humidity, ph, rainfall]

    Returns:
    str: The predicted crop.
    """
    # Load the trained model with the correct path
    model_path = os.path.join(os.path.dirname(__file__), 'svm_trained_model.joblib')
    model = joblib.load(model_path)
    
    # Ensure the input data is a 2D array with shape (1, 7)
    input_data = np.array(input_data).reshape(1, -1)
    
    # Predict the crop
    predicted_crop = model.predict(input_data)
    
    return predicted_crop[0]



input_data = np.array([90, 40, 40, 20.5, 82, 6.5, 202])
my_prediction = predict_crop(input_data)
print(my_prediction)