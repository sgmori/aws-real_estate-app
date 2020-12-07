from flask import Flask, request, render_template

application = app = Flask(__name__)

@application.route('/')
def index():
    return "This is the main page."

@application.route('/showLineChart')
def line():
    return render_template('index.html')

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