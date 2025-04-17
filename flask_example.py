# Import packages
from flask import Flask, jsonify, request

# Create a Flash App object
app = Flask(__name__)

# Define the URL route & function to apply
@app.route('/greet', methods=['GET'])

# Define a function called 'greet_user'
def greet_user():
  # Define name as being the extracted name (or Guest if not found)
    name = request.args.get('name', 'Guest')
  # Return a formatted JSON message that says 'Hello, user' based on name
    return jsonify({'message': f'Hello, {name}!'})

# Only run if the file is run directly (with error message if issue)
if __name__ == '__main__':
    app.run(debug=True)

