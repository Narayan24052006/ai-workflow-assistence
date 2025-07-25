# backend/app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from workflow import app_graph

# Load environment variables (for API keys)
load_dotenv()

app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for the React app
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/execute-workflow', methods=['POST'])
def execute_workflow():
    data = request.get_json()
    if not data or 'task' not in data:
        return jsonify({"error": "Task is required"}), 400

    task = data['task']
    
    # The initial state to start the graph
    initial_state = {"task": task}

    try:
        # Run the graph and get the final state
        final_state = app_graph.invoke(initial_state)
        return jsonify(final_state)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure you have a .env file with your GEMINI_API_KEY
    if not os.environ.get("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY not found in .env file")
    app.run(port=5000, debug=True)