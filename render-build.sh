#!/usr/bin/env bash

# pip 업데이트
python -m pip install --upgrade pip

# Update package manager
sudo apt-get update -y

# sudo apt-get install -y portaudio19-dev
# pip install sounddevice
# pip3 install pipwin
# pip3 install pyaudio

# Install PortAudio development libraries
# apt-get install -y portaudio19-dev
# apt-get install -y portaudio19-dev build-essential libsndfile1 libasound2-dev


# Run pip installation
pip install -r requirements.txt
