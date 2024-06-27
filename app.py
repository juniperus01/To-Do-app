from bson import ObjectId
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from pymongo import MongoClient

from models import User, Item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fca5b60df8d349cb9f5828b9531cadd0'
app.config['JWT_SECRET_KEY'] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

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


# Create a new item
@app.route('/item', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    current_user_email = get_jwt_identity()

    item = Item(data['name'], data['description'], created_by=current_user_email)

    db.items.insert_one(item.to_dict())
    return jsonify(message="Item created successfully"), 201


# Retrieve a list of all items
@app.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    items = db.items.find()
    items_list = [{"id": str(item["_id"]), "name": item["name"], "description": item["description"], "created_at": item["created_at"]} for item in items]
    return jsonify(items=items_list), 200


# Retrieve a specific item by ID
@app.route('/item/<item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    item = db.items.find_one({"_id": ObjectId(item_id)})
    if item:
        item_data = {"id": str(item["_id"]), "name": item["name"], "description": item["description"], "created_at": item["created_at"]}
        return jsonify(item=item_data), 200
    else:
        return jsonify(message="Item not found"), 404


# Update an existing item
@app.route('/item/<item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    update_data = {}
    if 'name' in data:
        update_data['name'] = data['name']
    if 'description' in data:
        update_data['description'] = data['description']
    
    result = db.items.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    if result.matched_count > 0:
        return jsonify(message="Item updated successfully"), 200
    else:
        return jsonify(message="Item not found"), 404


# Delete an item
@app.route('/item/<item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    result = db.items.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count > 0:
        return jsonify(message="Item deleted successfully"), 200
    else:
        return jsonify(message="Item not found"), 404
