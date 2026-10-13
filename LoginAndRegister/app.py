from flask import Flask, jsonify, request

from werkzeug.security import (
    generate_password_hash,
     check_password_hash
)
from flask_jwt_extended import (
     JWTManager,
     create_access_token,
     get_jwt_identity,
      jwt_required,
      get_jwt
)

from datetime import timedelta

app = Flask(__name__)

# Initialize JWT with flask
jwt = JWTManager(app)

app.config["JWT_SECRET_KEY"] = "jwt-secret-access-token"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

users = {}

# Register
@app.route("/register", methods = ["POST"])
def register():

    if not request.is_json:
        return jsonify({
            "error":"Request must be json"
        }), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "Error": "Invalid JSON"
        }), 400

    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not isinstance(username, str) or not username.strip():
        return jsonify({
            "Error":"Invalid username"
        }), 400

    if not isinstance(password, str) or len(password) < 8:
        return jsonify({
            "Error": "Password must contain at least 8 characters"
        }), 400

    username = username.strip().lower()
    email = email.strip().lower()

    if username in users:
        return jsonify({
            "Error": "Username already Exists"
        }), 400

    for user in users:
        if user["email"] == email:
            return jsonify({
                "Error": "Email already Exists"
            }), 400

    users[username] = {
        "email": email,
        "password": generate_password_hash(password),
        "role": "student"
    }

    return jsonify({
        "message": "Registration is successful",
        "username": username,
        "email": email
    }), 201


#Login API
@app.route("/login", methods =["POST"])
def login():

    if not request.is_json:
        return jsonify({
            "error": "Request must be JSON"
        }), 400
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid JSON"
        }), 400

    username = data.get("username")
    password = data.get("password")

    username = username.strip().lower()
    user = users.get(username)
    # verify the password
    if not user or not check_password_hash(user["password"], password):
         return jsonify({
             "Error": "Invalid username or password",
             "username": username,
             "password": password

         }), 401
    # Generate JWT after successful Authentication
    access_token = create_access_token(
        identity=username,
        additional_claims= {"role": user["role"]}
    )

    return jsonify({
        "Message": "login successful",
        "access_token": access_token
    }),200

# Protected profile API
@app.route("/profile",methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()
    claims = get_jwt()

    if claims.get("role") != "student":
        return jsonify({
            "message": "Access allowed for students only"
        })
    user = users.get(current_user)

    if user is None:
        return jsonify({
            "error":"User not found"
        }), 404

    return jsonify({
        "username": current_user,
        "email": user["email"],
        "role": user["role"]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)