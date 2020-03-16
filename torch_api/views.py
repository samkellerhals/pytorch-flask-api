from torch_api import api
from flask import request
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World'}

    def post(self):
        body = request.get_json()
        return {'you sent': body}, 201

class PredictImage(Resource):
    def post(self):
        body = request.get_json()
        return {
            'class_id':'xxx',
            'class_name': 'xxx'
            }

api.add_resource(HelloWorld, '/')
api.add_resource(PredictImage, '/predict')