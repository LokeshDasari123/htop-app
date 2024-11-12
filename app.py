from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Lokesh Dasari"  # Replace with your full name
    username = "Lokesh Dasari"
    server_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z")
    top_output = subprocess.check_output("top -b -n 1", shell=True).decode("utf-8")

    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <p><Strong> Top Output</strong></p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
