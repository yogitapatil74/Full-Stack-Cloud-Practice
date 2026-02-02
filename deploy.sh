#!/bin/bash

echo "Starting Deployment Pipeline..."

# 1. Update system packages
sudo apt update -y

# 2. Install Python and Pip
sudo apt install python3-pip -y

# 3. Install Flask (The core framework for our Full Stack app)
pip3 install flask

# 4. Kill any old versions of the app running on port 5000 (Prevents errors)
fuser -k 5000/tcp || true

# 5. Run the application in the background
nohup python3 app.py > output.log 2>&1 &

echo "Deployment Successful! The Elegant Dashboard is live on port 5000."
echo "Check your EC2 Public IP to see the result."
