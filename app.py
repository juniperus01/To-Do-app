from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fca5b60df8d349cb9f5828b9531cadd0'
jwt = JWTManager(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.myDatabase


# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to ToDo app!")


if __name__ == '__main__':
    app.run(debug=True)
