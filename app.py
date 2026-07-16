import os
from flask import Flask, render_template, send_file, abort

app = Flask(__name__)

# Serve the main dashboard interface
@app.route('/')
def index():
    return render_template('dashboard.html')

# Secure route to load and display absolute image filepaths from the machine
@app.route('/local-evidence/<path:filepath>')
def serve_local_image(filepath):
    # Normalize Windows and Linux paths
    normalized_path = os.path.normpath(filepath)
    
    # Check if file exists before trying to send it
    if os.path.exists(normalized_path) and os.path.isfile(normalized_path):
        return send_file(normalized_path)
    else:
        return "Evidence image not found at specified path.", 404

if __name__ == '__main__':
    print("[INFO] Starting Flask Frontend Dashboard on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)