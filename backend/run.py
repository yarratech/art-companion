from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/welcome', methods=['GET'])
def welcome_message():
    return jsonify({"message": "Welcome to the AI Art Assistant!"})

if __name__ == '__main__':
    app.run(debug=True)
