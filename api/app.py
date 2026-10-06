# from flask import Flask, jsonify
#
# app = Flask(__name__) # creates our Flask Application
#
# @app.route("/students")
# def home():
#     # return "Hello REST APIs"
#     data = {
#         "name":"Rupa"
#     }
#
#     return jsonify((data))
#
# @app.route("/students/<int:id>") # path parameter in angular braces
# def get_student(id):
#     # return "Hello REST APIs"
#
#     if id == 101:
#         data = {
#             "id": 101,
#             "name": "ALice"
#         }
#
#     return jsonify(data)
#
#
# if __name__ == "__main__":    # starts the server
#     app.run(debug=True)