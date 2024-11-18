import speech_recognition as sr
import pyperclip
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Python Web App</h1>"
def recognize_speech_from_microphone():
    # Recognizer와 Microphone 객체 초기화
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:  # 무한 루프를 사용하여 계속 음성을 인식
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # 주변 소음에 적응
            
            try:
                # 음성을 인식하는 최대 시간 설정 (예: 10초)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                
                # Google Speech Recognition을 사용하여 음성을 텍스트로 변환
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"You said: {text}")  # 출력
                pyperclip.copy(text)  # 클립보드에 복사

                # 텍스트 입력이 'stop'이라면 종료
                if text.lower() == "stop":
                    print("Exiting...")
                    break

            except sr.WaitTimeoutError:
                print("Listening timed out, no speech detected.")  # 음성이 일정 시간 내에 들어오지 않음
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")  # 음성을 인식하지 못함
            except sr.RequestError as e:
                print(f"Could not request results; {e}")  # Google API 요청 오류 처리
recognize_speech_from_microphone()
      