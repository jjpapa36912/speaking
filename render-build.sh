#!/usr/bin/env bash

# pip 업데이트
python -m pip install --upgrade pip
# pip install portaudio
pip install --upgrade pip setuptools wheel



# Update package manager
apt-get update -y
# apt-get install portaudio19-dev python3-pyaudio
# apt-get install portaudio19-dev python-all-dev
# apt-get install portaudio19-dev
# apt-get install portaudio19-dev  # portaudio 개발 파일 설치
# apt-get install python3-pyaudio  # PyAudio 설치
# pip install python3-pyaudio
# pip3 install pyaudio
# PortAudio 빌드 및 설치
cd $HOME
git clone https://github.com/PortAudio/portaudio.git
cd portaudio
./configure --prefix=$HOME/.local
make
make install

# 환경 변수 설정
export CFLAGS="-I$HOME/.local/include"
export LDFLAGS="-L$HOME/.local/lib"
export LD_LIBRARY_PATH="$HOME/.local/lib:$LD_LIBRARY_PATH"

# PyAudio 설치
pip install --no-binary :all: pyaudio
# # PyAudio 설치
# pip install --no-binary :all: --global-option="build_ext" --global-option="-I$HOME/.local/include" --global-option="-L$HOME/.local/lib" pyaudio


# sudo apt-get install -y portaudio19-dev
# pip install sounddevice
# pip3 install pipwin
# pip3 install pyaudio

# Install PortAudio development libraries
# apt-get install -y portaudio19-dev
# apt-get install -y portaudio19-dev build-essential libsndfile1 libasound2-dev


# Run pip installation
pip install -r requirements.txt
