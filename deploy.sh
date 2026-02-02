#!/bin/bash
echo "Initializing Deployment..."
# Update system
sudo apt update -y
# Install Python environment
sudo apt install python3-pip python3-venv -y
# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
# Install Flask
pip install flask
nohup python3 app.py > output.log 2>&1 &
echo "Application is now running on port 5000."
