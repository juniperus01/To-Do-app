from flask import Flask, jsonify
from pymongo import MongoClient
from auth import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize MongoClient and Database
client = MongoClient('mongodb://localhost:27017/')
db = client.ToDo_database


# Home route
@app.route('/')
def home():
    return jsonify(message="Welcome to ToDo app!")


if __name__ == '__main__':
    app.run(debug=True)
