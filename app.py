from meme import GetMeme
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

app = Flask(__name__) 
api = Api(app) 

class Send(Resource):
    def post(self):
        query = request.get_json()

        x = GetMeme(*query.values())
        try:

            return x['data']['url']
        except:
            return "template not found"
            
api.add_resource(Send, '/')
if __name__ == '__main__': 
    app.run(debug = True) 
