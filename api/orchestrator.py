from flask import Flask, request, jsonify
import os
from supabase_manager import SupabaseManager
from my_agent import MyAgent
from agent_orchestrator import AgentOrchestrator # Import the orchestrator class

app = Flask(__name__)

# Initialize AgentOrchestrator globally (or per request, depending on state management needs)
orchestrator = AgentOrchestrator()

@app.route('/orchestrate', methods=['POST'])
def orchestrate_agent():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    agent_id = data.get('agent_id')
    user_query = data.get('user_query')
    conversation_id = data.get('conversation_id')

    if not agent_id or not user_query:
        return jsonify({"error": "'agent_id' and 'user_query' are required"}), 400

    # Process the request using the AgentOrchestrator
    # The orchestrator will handle loading/saving agent state and interacting with RAG/Gemini
    try:
        gemini_response = orchestrator.process_request(agent_id, user_query, conversation_id)
        return jsonify({"status": "success", "agent_response": gemini_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # This block is for local testing only. Vercel will run the app via a WSGI server.
    app.run(debug=True, port=5000)
