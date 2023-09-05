import os
import urllib.request

execution_path = os.getcwd()
model_dir = os.path.join(execution_path, "models")

# Define the URL for the pre-trained model weights
model_url = "https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth"

# Specify the directory where you want to save the model weights
model_dir = os.path.join(execution_path, "models")

# Ensure the directory exists, or create it if necessary
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Specify the full path for the model weights file
model_path = os.path.join(model_dir, "retinanet_resnet50_fpn_coco-eeacb38b.pth")

# Download the model weights from the URL
urllib.request.urlretrieve(model_url, model_path)

# Set the model path to the downloaded weights
#detector.setModelPath(model_path)

# No