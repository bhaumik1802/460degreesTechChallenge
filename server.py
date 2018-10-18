#!/usr/bin/python

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(Helloworld, '/')

if __name__ == '__main__':
     app.run(host = '127.0.0.1', port='5002')