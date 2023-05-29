import speech_recognition as sr
import pyaudio

# Создаем объект Recognizer
r = sr.Recognizer()

# Записываем аудио с микрофона
with sr.Microphone() as source:
    print("Говорите сейчас...")
    audio = r.listen(source)

try:
    # Распознаем речь с помощью Google Speech Recognition
    text = r.recognize_google(audio, language="ru")
    print("Вы сказали: " + text)
except sr.UnknownValueError:
    print("Не удалось распознать речь")
except sr.RequestError as e:
    print("Ошибка сервиса распознавания речи; {0}".format(e))