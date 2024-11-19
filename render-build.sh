#!/usr/bin/env bash

# pip 업데이트
python -m pip install --upgrade pip
# pip install portaudio



# Update package manager
apt-get update -y
apt-get install portaudio19-dev python3-pyaudio
# apt-get install portaudio19-dev python-all-dev
# apt-get install portaudio19-dev
# apt-get install portaudio19-dev  # portaudio 개발 파일 설치
# apt-get install python3-pyaudio  # PyAudio 설치
# pip install python3-pyaudio
pip3 install pyaudio


# sudo apt-get install -y portaudio19-dev
# pip install sounddevice
# pip3 install pipwin
# pip3 install pyaudio

# Install PortAudio development libraries
# apt-get install -y portaudio19-dev
# apt-get install -y portaudio19-dev build-essential libsndfile1 libasound2-dev


# Run pip installation
pip install -r requirements.txt
