import os
from flask import Flask, render_template, jsonify, request

# Force Flask to locate the templates folder inside the active directory
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

# Student roster database records
STUDENTS_DATABASE = [
    {"name": "Alex Henderson", "reg_id": "REG-2026-0041", "seat": "Zone 1 (Row 1, Seat A)", "score": 98, "status": "Attentive"},
    {"name": "Sarah Miller", "reg_id": "REG-2026-0042", "seat": "Zone 2 (Row 1, Seat B)", "score": 85, "status": "Warned"},
    {"name": "John Doe", "reg_id": "REG-2026-0043", "seat": "Zone 3 (Row 2, Seat B)", "score": 62, "status": "Suspended"}
]

@app.route('/')
def dashboard():
    # Renders templates/dashboard.html
    return render_template('dashboard.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    # API Endpoint: Returns JSON formatted student roster details
    return jsonify(STUDENTS_DATABASE)

@app.route('/api/trigger-alert', methods=['POST'])
def trigger_alert():
    # API Endpoint: Called by the AI engine when behavior is detected
    data = request.json
    print(f"[AI ALERT RECEIVED] Activity: {data.get('activity')} detected for Student: {data.get('student_id')}")
    return jsonify({"status": "success", "message": "Alert propagated to front-end database."})

if __name__ == '__main__':
    print("[INFO] Starting Flask Backend Server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)