from torch_api import api
from flask import request
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World'}

    def post(self):
        body = request.get_json()
        return {'you sent': body}, 201

api.add_resource(HelloWorld, '/')