from flask import Flask, jsonify, request

app = Flask(__name__)

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
        "password": password,
        "role": "student"
    }

    return jsonify({
        "message": "Registration is successful",
        "username": username,
        "email": email
    }), 201




if __name__ == "__main__":
    app.run(debug=True)