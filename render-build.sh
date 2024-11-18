#!/usr/bin/env bash
# Update package manager
apt-get update -y

# Install PortAudio development libraries
apt-get install -y portaudio19-dev

# Run pip installation
pip install -r requirements.txt
