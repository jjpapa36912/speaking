#!/usr/bin/env bash

# pip 업데이트
python -m pip install --upgrade pip
# Update package manager
apt-get update -y

# Install PortAudio development libraries
apt-get install -y portaudio19-dev

# Run pip installation
pip install -r requirements.txt
