from flask import Flask, request, jsonify, session
from flask_session import Session
from db import usersdb
from flask_cors import CORS

app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions on the filesystem
Session(app)
users_db = usersdb()
cors=CORS(app)

@app.route("/api/signup", methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('name') 
    email = data.get('email')
    password = data.get('password')
    phone=data.get('phone')
    docID = data.get('docID')
    carType =data.get('carType')
    carModel =data.get('carModel')
    carLetters = data.get('carLetters')
    carChassis = data.get('carChassis')
    docSource =data.get('docSource')
    address =data.get('address')
    carNumbers = data.get('carNumbers')

    try:
        users_db.signUp(username, email, password,phone,docID,docSource,carType,carModel,carLetters,carChassis,carNumbers,address)
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user_id = users_db.login(email, password)
    if user_id:
        session['user_id'] = user_id  # Store user_id in session
        return jsonify({"message": "Login successful!", "user_id": user_id}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@app.route("/api/update_password", methods=['POST'])
def update():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('new_password')

    try:
        users_db.edit(email, new_password)
        return jsonify({"message": "Password updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/logout", methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    return jsonify({"message": "Logged out successfully!"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
