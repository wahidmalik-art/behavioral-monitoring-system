import time
import requests

print("[AI ENGINE] Behavior monitoring active...")

while True:
    # Simulating the AI detecting behavior
    time.sleep(10)
    print("[AI ENGINE] Detected student behavior. Sending alert to dashboard...")
    
    # Send the alert to your Flask app
    try:
        requests.post('http://127.0.0.1:5000/api/trigger-alert', json={
            "student_id": "REG-2026-0043",
            "activity": "Suspicious Movement"
        })
    except:
        print("[AI ENGINE] Could not connect to dashboard. Is app.py running?")