from torch_api import api
from flask import request, make_response
from flask_restful import Resource 
from torch_api.model import get_prediction
import werkzeug
import requests
from PIL import Image
import wget
import os
import glob
import imghdr

class Home(Resource):
    def get(self):
        return make_response('<h1>Pytorch-Flask-Api Server</h1><br><span><b>Status:</b> Running</span>', 200)

class PredictImage(Resource):
    def post(self):
        image_urls = request.get_json(force=True)
        img_folder = 'torch_api/img/'
        predictions = []

        # clean-up (delete all images in directory)
        folder = glob.glob(img_folder + '*')
        for f in folder:
            os.remove(f)
        
        # download all relevant images into folder
        for i in range(len(image_urls)):
            image_name = image_urls[i]
            wget.download(image_urls[i], out=img_folder + 'image' + str(i) + '.jpg')

        # make prediction for all items (except for non JPG images)
        for i in range(len(os.listdir(img_folder))):
            f = open(img_folder + 'image' + str(i) + '.jpg', 'rb')
            # Check filetype
            if imghdr.what(f) == 'jpeg':
                img_bytes = f.read()
                f.close()
                preds = get_prediction(img_bytes)
                preds_dict = {'image' : str(i), 'class' : preds[1]}
                predictions.append(preds_dict)
            else:
                preds_dict = {'image' : str(i), 'class' : 'Error: JPEG supported only.'}
                predictions.append(preds_dict)
    
        # clean-up (delete all images in directory)
        folder = glob.glob(img_folder + '*')
        for f in folder:
            os.remove(f)

        return predictions, 200

api.add_resource(Home, '/')
api.add_resource(PredictImage, '/predict')