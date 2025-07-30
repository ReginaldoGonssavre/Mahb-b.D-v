import speech_recognition as sr
import subprocess

# This is a conceptual example. You would need to install the necessary libraries
# and have a model like Qwen running.

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_whisper(audio, model="base.en")
        return text
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Whisper; {e}")
    return None

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == '__main__':
    while True:
        command = listen()
        if command:
            print(f"Executing: {command}")
            if "exit" in command:
                break
            execute_command(command)