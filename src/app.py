from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Flask app! Visit /login or /user/<id>."

# Insecure: Debug mode is enabled
app.config['DEBUG'] = True

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Insecure: Using hardcoded credentials
    if username == "admin" and password == "password123":
        return jsonify({"message": "Logged in!"}), 200

    # Insecure: Returning user-supplied data without sanitization
    return jsonify({"error": f"Invalid credentials for {username}"}), 401

# SQL injection vulnerability
@app.route('/user/<user_id>')
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Insecure
    return jsonify({"query": query})

# Insecure: Missing CSRF token
@app.route('/update_profile', methods=['POST'])
def update_profile():
    user_data = request.form.to_dict()
    # Simulated profile update
    return jsonify({"status": "Profile updated!", "data": user_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
