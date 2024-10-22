from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = [{"id": 1, "name": "Sample Task"}]
    return jsonify(tasks)

@app.route('/api/', methods=['GET'])
def get_status():
    tasks = [{"trial": "running"}]
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
