from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Home Route
@app.route('/')
def home():
    return "User Management System"

# Get All Users
@app.route('/users', methods=['GET'])
def get_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

# Get User by ID
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    else:
        return "User not found", 404

# Create New User
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = json.loads(request.data)
        name = data['name']
        email = data['email']
        password = data['password']

        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        return "User created", 201
    except Exception as e:
        return str(e), 400

# Update User
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = json.loads(request.data)
    name = data.get('name')
    email = data.get('email')

    if name and email:
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        conn.commit()
        return "User updated"
    else:
        return "Invalid data", 400

# Delete User
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return f"User {user_id} deleted"

# Search Users by Name
@app.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return "Please provide a name to search", 400

    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    users = cursor.fetchall()
    return jsonify(users)

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    if user:
        return jsonify({"status": "success", "user_id": user[0]})
    else:
        return jsonify({"status": "failed"}), 401

# Run the Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
