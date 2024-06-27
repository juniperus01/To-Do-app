# Flask To-Do App with JWT Authentication

This is a Flask-based To-Do application that demonstrates basic CRUD operations with JWT (JSON Web Token) authentication.

## Pre-requisites

Before running the application, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- MongoDB

## Setting Up

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/juniperus01/To-Do-app.git
   cd To-Do-app
   ```

2. **Create and activate a virtual environment:**
  
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

3. **Install dependencies:**

  ```bash
  pip install -r requirements.txt
  ```

4. **Set environment variables:**

Create a .env file in the root directory with the following variables:

  ```bash
  SECRET_KEY=your_secret_key_here
  MONGO_URI=mongodb://localhost:27017/myDatabase # Replace your_secret_key_here with a secret key for your Flask application.
  ```

5. Initialize MongoDB:

Ensure MongoDB is running locally. If not, start it using:

  ```bash
  mongod
  ```
This assumes MongoDB is listening on localhost:27017.

6. Run the application:
  ```bash
  flask run
  ```
The application should now be running locally at http://localhost:5000.

## JWT Authentication

1. Register a User:

Send a POST request to /register with JSON data containing email and password fields.

Example:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "password123"}' http://localhost:5000/register
  ```

2. Login:

Send a POST request to /login with JSON data containing email and password fields.

Example:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "password123"}' http://localhost:5000/login
  ```

This will return an access token that you can use for authenticated requests.

## API Endpoints


1. Create an Item:

  ```bash
    POST /item
    Header: Authorization: Bearer <your_access_token>
    Body: {"name": "Item Name", "description": "Item Description"}
```

2. Get All Items:

  ```bash
    GET /items
    Header: Authorization: Bearer <your_access_token>
  ```

3. Get a Specific Item:
   
  ```bash
  GET /item/<item_id>
  Header: Authorization: Bearer <your_access_token>
  ```

4. Update an Item:

  ```bash
    PUT /item/<item_id>
    Header: Authorization: Bearer <your_access_token>
    Body: {"name": "Updated Name", "description": "Updated Description"}
  ```

5. Delete an Item:
  ```bash
    DELETE /item/<item_id>
    Header: Authorization: Bearer <your_access_token>
