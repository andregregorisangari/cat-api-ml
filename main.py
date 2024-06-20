import os
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from io import BytesIO
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debugging: Print loaded environment variables
print("GCS_BUCKET_NAME:", os.getenv("GCS_BUCKET_NAME"))
print("CREDENTIALS_PATH:", os.getenv("CREDENTIALS_PATH"))

# Get the bucket name and credentials path from environment variables
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH")

# Temporary client to download the credentials file
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    temp_client = storage.Client.create_anonymous_client()
    bucket = temp_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

# Download credentials from GCS and set the GOOGLE_APPLICATION_CREDENTIALS environment variable
if GCS_BUCKET_NAME and CREDENTIALS_PATH:
    download_blob(GCS_BUCKET_NAME, CREDENTIALS_PATH, "gcs.json")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcs.json"
else:
    raise ValueError("GCS_BUCKET_NAME or CREDENTIALS_PATH is not set")

# Create a storage client using the downloaded credentials
credentials = service_account.Credentials.from_service_account_file("gcs.json")
storage_client = storage.Client(credentials=credentials)

app = Flask(__name__)
app.config["ALLOWED_EXTENSIONS"] = set(['png', 'jpg', 'jpeg'])

# Paths to the model and labels in the GCS bucket
MODEL_PATH = 'models/cat_model.h5'
LABELS_PATH = 'models/labels.txt'

# Download model and labels from GCS
download_blob(GCS_BUCKET_NAME, MODEL_PATH, "cat_model.h5")
download_blob(GCS_BUCKET_NAME, LABELS_PATH, "labels.txt")

# Load model
model = load_model("cat_model.h5", compile=False)

# Load labels
with open("labels.txt", "r") as file:
    labels = file.read().splitlines()

# List of cat breeds
cat_breeds = [
    'Abyssinian',
    'American Bobtail',
    'American Shorthair',
    'Bengal',
    'Birman',
    'Bombay',
    'British Shorthair',
    'Egyptian Mau',
    'Maine Coon',
    'Persian',
    'Ragdoll',
    'Russian Blue',
    'Siamese',
    'Sphynx',
    'Tuxedo'
]

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

def preprocess_input_image(image_file):
    img = Image.open(image_file).convert('RGB')
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def predict_cat_breed(img_array):
    predictions = model.predict(img_array)
    predicted_label = labels[np.argmax(predictions)]
    confidence = float(predictions[0][np.argmax(predictions)])
    return predicted_label, confidence

@app.route('/')
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None,
    }), 200

@app.route("/prediction", methods=["POST"])
def prediction():
    if request.method == "POST":
        if "image" not in request.files:
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Bad Request, no image part",
                },
                "data": None,
            }), 400

        image_file = request.files["image"]

        if image_file.filename == "" or not allowed_file(image_file.filename):
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Bad Request, unsupported file format or no selected file",
                },
                "data": None,
            }), 400

        # Preprocess image
        img_array = preprocess_input_image(image_file)

        # Make prediction
        predicted_label, confidence = predict_cat_breed(img_array)

        # Check confidence threshold
        if confidence >= 0.5:
            predicted_breed_info = {}
            if predicted_label in cat_breeds:
                predicted_breed_info = {
                    "breed_name": predicted_label,
                }
            return jsonify({
                "status": {
                    "code": 200,
                    "message": "Success Predict!",
                },
                "data": {
                    "cat_or_not_cat": "CAT",
                    "predicted_breed_info": predicted_breed_info,
                    "confidence": confidence,
                }
            }), 200
        else:
            return jsonify({
                "status": {
                    "code": 200,
                    "message": "Image is unclear or not a cat",
                },
                "data": {
                    "cat_or_not_cat": "NOT CAT",
                    "confidence": confidence,
                }
            }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
