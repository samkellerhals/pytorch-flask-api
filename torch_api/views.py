from torch_api import api
from flask import request
from flask_restful import Resource, reqparse
from torch_api.model import get_prediction
import werkzeug

class PredictImage(Resource):
    def post(self):
        files = request.files # get all files
        images = files.getlist('image') # get list of images
        
        predictions = []

        for i in range(len(images)): # make predictions for each image
            img_bytes = images[i].read()
            preds = get_prediction(img_bytes)
            preds_dict = {'image' : str(i), 'class' : preds[1]}
            predictions.append(preds_dict)

        return predictions, 200

api.add_resource(PredictImage, '/predict')