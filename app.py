from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from pymongo import MongoClient

from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fca5b60df8d349cb9f5828b9531cadd0'
jwt = JWTManager(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.toDoDatabase


# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to ToDo app!")


# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if db.users.find_one({"email": data['email']}):
        return jsonify(message="User already exists"), 400
    
    user = User(email=data['email'], password=data['password'])
    db.users.insert_one(user.to_dict())
    
    return jsonify(message="User registered successfully"), 201


# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_data = db.users.find_one({"email": data['email']})
    
    if not user_data:
        return jsonify(message="Invalid credentials : Email does not exist"), 401
    
    user = User.from_dict(user_data)
    
    if user.check_password(data["password"]):
        access_token = create_access_token(identity=data['email'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401