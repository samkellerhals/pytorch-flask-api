from io import BytesIO
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import json
import requests

# get model into evaluation mode
model = models.densenet121(pretrained=True).eval()
print('model was sucessfully loaded.')

# imagenet classes
imagenet_class_index = json.load(open('torch_api/imagenet_class_index.json'))

def transform_image(image_bytes):
    img_transforms = transforms.Compose([transforms.Resize(255),
                                     transforms.CenterCrop(224),
                                     transforms.ToTensor(),
                                     transforms.Normalize(
                                         [0.485, 0.456, 0.406],
                                         [0.229, 0.224, 0.225])])
                                         
    image = Image.open(BytesIO(image_bytes))
    return img_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]