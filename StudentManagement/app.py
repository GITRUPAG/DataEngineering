from flask import Flask, request, jsonify

app = Flask(__name__)

students = [

    {
        "id": 1,
        "name": "Ravi",
        "course": "Python"
    }
]

# Get all Students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students),200

@app.route("/students/<int:id>", methods = ["GET"])
def get_student(id):

    for student in students:

        if student["id"] == id:
            return jsonify(student), 200

    return jsonify({
        "message": "Student not Found!!"
    }), 404

# Post Student
@app.route("/students/add", methods=["POST"])
def add_student():

    data = request.get_json(silent=True)  # if json is empty it returns None

     # Rupa - weyrty - Rupa
    # Rupa - 7415cvbgfb
    # Rupa - 7415cvbgfb
    # Rupa  - 5245iuyfgh
    if data is None:
        return jsonify({
            "message:Invalid Json"
        })
    if "name" not in data:
        return jsonify({
            "message:Name is required"
        })

    if not isinstance(data["name"], str): # check whether value belongs to data type
        return jsonify({
            "message":"Name must be string"
        })


    new_student = {
        "id": len(students)+1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student), 201


@app.route("/students/update/<int:id>", methods =["PUT"])
def update_student(id):
    data = request.get_json()

    for student in students:

        if student["id"] == id:

            student["name"] = data["name"]
            student["course"] = data["course"]

            return jsonify(student), 200
    return jsonify({
        "message": "Student not found"
    }), 404

@app.route("/students/<int:id>", methods =["DELETE"])
def delete_student(id):

    for student in students:
        if student["id"] == id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted"
            }), 200
    return jsonify({
        "message": "Student not found"
    }), 404






if __name__ == "__main__":
    app.run(debug=True)