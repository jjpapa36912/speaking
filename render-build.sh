#!/usr/bin/env bash

# pip 업데이트
python -m pip install --upgrade pip

# Update package manager
apt-get update -y

apt-get install -y portaudio19-dev
pip3 install pipwin
# pip3 install pyaudio

# Install PortAudio development libraries
# apt-get install -y portaudio19-dev
# apt-get install -y portaudio19-dev build-essential libsndfile1 libasound2-dev


# Run pip installation
pip install -r requirements.txt
