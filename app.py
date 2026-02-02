from flask import Flask, render_template, jsonify
import platform
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # This dictionary gathers real system data to show on your elegant dashboard
    # Matches CV: "Managed Unix-like environments and monitored system status"
    system_info = {
        "os": platform.system(),
        "release": platform.release(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "location": "AWS EC2 Instance (Ubuntu)"
    }
    # This line tells Flask to look into the /templates folder for your HTML
    return render_template('index.html', info=system_info)

@app.route('/api/status')
def status():
    """API endpoint for health monitoring"""
    return jsonify({"status": "Cloud Server Operational", "code": 200})

if __name__ == "__main__":
    # host='0.0.0.0' makes the app visible to the internet on your EC2 instance
    app.run(host='0.0.0.0', port=5000, debug=True)
