#!/bin/bash
# Use this script for Setting up development on Cloud9

sudo pip install -r requirements.txt
sudo apt-get install postgresql


# For Deploying to Heroku
# Download and install the Heroku CLI
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh