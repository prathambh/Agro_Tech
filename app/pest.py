import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

# Define a function to predict pest from an image
def pred_pest(pest):
    model_path = os.path.join(os.path.dirname(__file__),'best_model.h5')
    model = load_model(model_path)
    try:
        # Load and preprocess the image
        img = image.load_img(pest, target_size=(64, 64))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Normalize pixel values (assuming your model expects normalized input)
        img_array = img_array / 255.0  # Adjust as per your model's preprocessing
        
        # Predict using the loaded model
        result = model.predict(img_array)
        
        # Assuming result is an array, return the predicted class (adjust as per your model output)
        predicted_class = np.argmax(result)  # Example: if result is probabilities, find the index of the max probability
        
        return predicted_class
    
    except Exception as e:
        print(f"Error predicting pest: {e}")
        return 'x'  # Return 'x' for any error case

# Example usage:
#pred = pred_pest('./static/pest1.jpg')
#print(pred)
