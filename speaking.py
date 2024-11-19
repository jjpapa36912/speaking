import speech_recognition as sr
import pyperclip
import sounddevice as sd
import numpy as np
import io
import wave
from flask import Flask, jsonify

app = Flask(__name__)


# 음성 데이터를 sounddevice를 사용하여 캡처
def listen_with_sounddevice(duration=10, fs=16000):
    # 음성을 저장할 numpy 배열
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # 음성 녹음이 끝날 때까지 대기
    return audio_data

@app.route('/')
def recognize_speech_from_microphone():
    # Recognizer와 Microphone 객체 초기화
    recognizer = sr.Recognizer()
    # microphone = sr.Microphone()
     # 마이크 객체 초기화
    # `device_index`는 기본 마이크를 사용할 수 있도록 설정
    # microphone = sr.Microphone(device_index=None)
    audio_data = listen_with_sounddevice()
    with io.BytesIO() as audio_io:
        with wave.open(audio_io, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit samples
            wf.setframerate(16000)
            wf.writeframes(audio_data.tobytes())
        audio_io.seek(0)
        audio_file = sr.AudioFile(audio_io)
        
        try:
            # 음성 파일을 인식기로 전달
            with audio_file as source:
                audio = recognizer.record(source)  # 음성 데이터 읽기

            # Google API로 음성 인식
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"You said: {text}")
            pyperclip.copy(text)  # 클립보드에 텍스트 복사
            return jsonify({"speech": text, "clipboard": "Text copied to clipboard"})
        except sr.WaitTimeoutError:
            print("Listening timed out, no speech detected.")
            return jsonify({"error": "Timeout, no speech detected"})
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return jsonify({"error": "Could not understand the audio"})
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return jsonify({"error": f"Request error: {e}"})
    # with microphone as source:
    #     print("Listening...")
    #     recognizer.adjust_for_ambient_noise(source)  # 주변 소음에 적응
    #     try:
    #         # 음성을 인식하는 최대 시간 설정 (예: 10초)
    #         audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

    #         # Google Speech Recognition을 사용하여 음성을 텍스트로 변환
    #         text = recognizer.recognize_google(audio, language="en-US")
    #         print(f"You said: {text}")  # 출력

    #         # 텍스트를 클립보드에 복사
    #         pyperclip.copy(text)

    #         return jsonify({"speech": text, "clipboard": "Text copied to clipboard"})

    #     except sr.WaitTimeoutError:
    #         print("Listening timed out, no speech detected.")  # 음성이 일정 시간 내에 들어오지 않음
    #         return jsonify({"error": "Timeout, no speech detected"})
    #     except sr.UnknownValueError:
    #         print("Sorry, I could not understand the audio.")  # 음성을 인식하지 못함
    #         return jsonify({"error": "Could not understand the audio"})
    #     except sr.RequestError as e:
    #         print(f"Could not request results; {e}")  # Google API 요청 오류 처리
    #         return jsonify({"error": f"Request error: {e}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)


# import speech_recognition as sr
# import pyperclip
# from flask import Flask, jsonify, request
# import sounddevice as sd

# app = Flask(__name__)

# # 'sounddevice'로 마이크 설정을 대신할 수 있습니다.
# def get_microphone():
#     return sr.Microphone(device_index=None)  # device_index를 지정하지 않으면 기본 장치 사용

# @app.route('/', methods=['POST'])
# def recognize_speech_from_microphone():
#     # Recognizer와 Microphone 객체 초기화
#     recognizer = sr.Recognizer()
#     microphone = get_microphone()

#     try:
#         with microphone as source:
#             print("Listening...")
#             recognizer.adjust_for_ambient_noise(source)  # 주변 소음에 적응

#             # 음성을 인식하는 최대 시간 설정 (예: 10초)
#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            
#             # Google Speech Recognition을 사용하여 음성을 텍스트로 변환
#             text = recognizer.recognize_google(audio, language="en-US")
#             print(f"You said: {text}")  # 출력
#             pyperclip.copy(text)  # 클립보드에 복사

#             # 텍스트 입력이 'stop'이라면 종료
#             if text.lower() == "stop":
#                 return jsonify({"message": "Exiting..."})

#             return jsonify({"text": text})

#     except sr.WaitTimeoutError:
#         return jsonify({"error": "Listening timed out, no speech detected."}), 408  # 타임아웃 오류
#     except sr.UnknownValueError:
#         return jsonify({"error": "Sorry, I could not understand the audio."}), 400  # 음성 인식 실패
#     except sr.RequestError as e:
#         return jsonify({"error": f"Could not request results; {e}"}), 500  # API 요청 오류 처리

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=10000)

# import speech_recognition as sr
# import pyperclip
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/recognize', methods=['POST'])
# def recognize_speech_from_microphone():
#     # Recognizer와 Microphone 객체 초기화
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     # 클라이언트가 보낸 오디오 데이터를 가져옵니다.
#     try:
#         with microphone as source:
#             print("Listening...")
#             recognizer.adjust_for_ambient_noise(source)  # 주변 소음에 적응

#             # 음성을 인식하는 최대 시간 설정 (예: 10초)
#             audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            
#             # Google Speech Recognition을 사용하여 음성을 텍스트로 변환
#             text = recognizer.recognize_google(audio, language="en-US")
#             print(f"You said: {text}")  # 출력
#             pyperclip.copy(text)  # 클립보드에 복사

#             # 텍스트 입력이 'stop'이라면 종료
#             if text.lower() == "stop":
#                 return jsonify({"message": "Exiting..."})

#             return jsonify({"text": text})

#     except sr.WaitTimeoutError:
#         return jsonify({"error": "Listening timed out, no speech detected."}), 408  # 타임아웃 오류
#     except sr.UnknownValueError:
#         return jsonify({"error": "Sorry, I could not understand the audio."}), 400  # 음성 인식 실패
#     except sr.RequestError as e:
#         return jsonify({"error": f"Could not request results; {e}"}), 500  # API 요청 오류 처리

# if __name__ == '__main__':
#     app.run(debug=True)


# import speech_recognition as sr
# import pyperclip
# from flask import Flask, request, jsonify

# app = Flask(__name__)


# @app.route('/')
# def recognize_speech_from_microphone():
#     # Recognizer와 Microphone 객체 초기화
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     while True:  # 무한 루프를 사용하여 계속 음성을 인식
#         with microphone as source:
#             print("Listening...")
#             recognizer.adjust_for_ambient_noise(source)  # 주변 소음에 적응
            
#             try:
#                 # 음성을 인식하는 최대 시간 설정 (예: 10초)
#                 audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                
#                 # Google Speech Recognition을 사용하여 음성을 텍스트로 변환
#                 text = recognizer.recognize_google(audio, language="en-US")
#                 print(f"You said: {text}")  # 출력
#                 pyperclip.copy(text)  # 클립보드에 복사

#                 # 텍스트 입력이 'stop'이라면 종료
#                 if text.lower() == "stop":
#                     print("Exiting...")
#                     break

#             except sr.WaitTimeoutError:
#                 print("Listening timed out, no speech detected.")  # 음성이 일정 시간 내에 들어오지 않음
#             except sr.UnknownValueError:
#                 print("Sorry, I could not understand the audio.")  # 음성을 인식하지 못함
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")  # Google API 요청 오류 처리
# # recognize_speech_from_microphone()


# if __name__ == '__main__':
#     app.run(debug=True)
      