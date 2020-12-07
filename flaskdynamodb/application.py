from flask import Flask, request
from flask_restful import Resource, Api

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World!'}
        
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask, jsonify
# import aws_controller
# import os

# application = app = Flask(__name__)

# @app.route('/')
# def index():
#     return "This is the main page."
    
# @app.route('/get-items')
# def get_items():
#     return jsonify(aws_controller.get_items())

# if __name__ == '__main__':
#     app.run()