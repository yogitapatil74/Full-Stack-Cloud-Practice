from flask import Flask, jsonify

app = Flask(__name__) 

@app.route('/')
def hello():
    # Sending a JSON object looks more like a real "Cloud API"
    return jsonify({
        "message": "Hello from AWS EC2!",
        "status": "Success",
        "environment": "Ubuntu/Linux"
    })

if __name__ == "__main__":
    # Added port 8080 because it's a common practice for cloud testing
    app.run(host='0.0.0.0', port=8080)
