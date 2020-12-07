from flask import Flask, request, render_template
import jsonify

application = Flask(__name__)

@application.route('/')
def index():
    return "This is the main page!"

@application.route('/test')
def line():
    return render_template('index.html')
    
@application.route('/echo/<name>')
def echo(name):
    val = {"new name": name}
    return jsonify(val)

if __name__ == '__main__':
    application.run(debug=True)





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