from io import BytesIO
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import json
import requests

url = 'https://natgeo.imgix.net/factsheets/thumbnails/01-hermit-crabs-minden_00512417.ngsversion.1547661601286.adapt.1900.1.jpg?auto=compress,format&w=1600&h=900&fit=crop'
response = requests.get(url)
model = models.densenet121(pretrained=True)
model.eval()
imagenet_class_index = json.load(open('imagenet_class_index.json'))

def transform_image(response):
    img_transforms = transforms.Compose([transforms.Resize(255),
                                     transforms.CenterCrop(224),
                                     transforms.ToTensor(),
                                     transforms.Normalize(
                                         [0.485, 0.456, 0.406],
                                         [0.229, 0.224, 0.225])])
                                         
    image = Image.open(BytesIO(response.content))
    return img_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]


print(get_prediction(response))

