import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# 1. Load the pre-trained MobileNetV2 model
# weights=MobileNet_V2_Weights.DEFAULT is the modern way to load pre-trained weights
model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)

# 2. Set the model to evaluation mode
model.eval()

# 3. Define the image transformation (Resizing and Normalization)
# MobileNetV2 expects 224x224 images normalized with specific means/stds
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 4. Load and preprocess your image
img = Image.open("your_image.jpg")
img_t = preprocess(img)
batch_t = torch.unsqueeze(img_t, 0) # Create a mini-batch as expected by the model

# 5. Perform inference (Feature Extraction)
with torch.no_grad():
    output = model(batch_t)

print(f"Feature Vector Shape: {output.shape}")
