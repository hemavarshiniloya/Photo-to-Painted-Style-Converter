from flask import Flask, request, jsonify
import base64
from PIL import Image
import io

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    image_data = data['image']

    # Decode the image
    image_data = image_data.split(",")[1]  # Remove the prefix
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))

    # Here you would add your model prediction logic
    # For demonstration, we will just return a mock prediction
    # Replace this with your model's prediction code
    prediction = "Mock Prediction"  # Replace with actual prediction logic

    return jsonify({'guess': prediction})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
